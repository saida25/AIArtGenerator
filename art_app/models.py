# art_app/models.py
from django.db import models
from django.contrib.auth.models import User

class GeneratedArt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    prompt = models.CharField(max_length=200, blank=True)
    seed = models.IntegerField()
    image_data = models.TextField()  # Base64 encoded image
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Art {self.id} by {self.user.username if self.user else 'Anonymous'}"