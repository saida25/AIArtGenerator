# art_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_optional
from django.http import JsonResponse
from django.conf import settings
import random
import json

from .models import GeneratedArt
from diffusion_model.diffusion import SimpleDiffusion, image_to_base64

# Initialize the diffusion model
diffusion_model = SimpleDiffusion(image_size=128, timesteps=100)

def home(request):
    """Home page with art generation form"""
    return render(request, 'home.html')

@login_optional
def generate_art(request):
    """Generate art based on parameters"""
    if request.method == 'POST':
        try:
            # Get parameters from request
            prompt = request.POST.get('prompt', '')
            seed = request.POST.get('seed')
            
            if seed:
                seed = int(seed)
            else:
                seed = random.randint(0, 1000000)
            
            # Generate the image
            image = diffusion_model.generate(seed=seed)
            image_base64 = image_to_base64(image)
            
            # Save to database if user is authenticated
            if request.user.is_authenticated:
                art = GeneratedArt.objects.create(
                    user=request.user,
                    prompt=prompt,
                    seed=seed,
                    image_data=image_base64
                )
            else:
                art = GeneratedArt.objects.create(
                    prompt=prompt,
                    seed=seed,
                    image_data=image_base64
                )
            
            return JsonResponse({
                'success': True,
                'image': image_base64,
                'seed': seed,
                'art_id': art.id
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def gallery(request):
    """Display gallery of generated artworks"""
    arts = GeneratedArt.objects.all().order_by('-created_at')[:20]
    return render(request, 'gallery.html', {'arts': arts})