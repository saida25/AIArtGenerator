# art_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('art_app.urls')),
]

# art_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_art, name='generate_art'),
    path('gallery/', views.gallery, name='gallery'),
]