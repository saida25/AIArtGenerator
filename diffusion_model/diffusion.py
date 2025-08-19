# diffusion_model/diffusion.py
import torch
import torch.nn as nn
import numpy as np
from PIL import Image
import io
import base64

class SimpleDiffusion:
    def __init__(self, image_size=64, timesteps=100):
        self.image_size = image_size
        self.timesteps = timesteps
        
        # Beta schedule (linear from 1e-4 to 0.02)
        self.betas = torch.linspace(1e-4, 0.02, timesteps)
        self.alphas = 1. - self.betas
        self.alpha_bars = torch.cumprod(self.alphas, dim=0)
    
    def forward_diffusion(self, x0, t):
        """Add noise to image at timestep t"""
        noise = torch.randn_like(x0)
        alpha_bar = self.alpha_bars[t]
        noisy_image = torch.sqrt(alpha_bar) * x0 + torch.sqrt(1 - alpha_bar) * noise
        return noisy_image, noise
    
    def generate(self, seed=None, steps=50):
        """Generate an image using a simplified diffusion process"""
        if seed is not None:
            torch.manual_seed(seed)
        
        # Start with random noise
        x = torch.randn(1, 3, self.image_size, self.image_size)
        
        # Simplified reverse process (not a trained model, just for demo)
        for t in range(steps-1, -1, -1):
            # In a real implementation, this would use a trained neural network
            # to predict the noise and subtract it
            alpha_bar = self.alpha_bars[t]
            estimated_noise = torch.randn_like(x) * 0.1  # Placeholder for real noise prediction
            
            # Remove a fraction of the noise
            x = (x - (1 - alpha_bar) * estimated_noise) / torch.sqrt(alpha_bar)
            
            # Add some randomness
            if t > 0:
                z = torch.randn_like(x)
                x = x + 0.1 * z  # Small amount of noise
        
        # Convert to image
        x = (x - x.min()) / (x.max() - x.min())  # Normalize to 0-1
        x = x.squeeze(0).permute(1, 2, 0).numpy()  # Change shape to HWC
        x = (x * 255).astype(np.uint8)  # Scale to 0-255
        
        return Image.fromarray(x)

# Utility function to convert image to base64 for web display
def image_to_base64(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")