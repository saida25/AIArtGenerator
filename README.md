# AI Art Generator

A Django-based web application that generates unique digital artwork using a simplified implementation of diffusion models. This project combines deep learning with web development to create an interactive art generation platform.

## Features

- **AI-Powered Art Generation**: Create unique digital artwork using a diffusion model
- **Customizable Parameters**: Control the generation with prompts and seed values
- **Art Gallery**: Browse previously generated artworks
- **User Authentication**: Save and manage your generated artworks (optional)
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Backend**: Django (Python web framework)
- **AI Model**: PyTorch-based diffusion model
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default, can be configured for others)
- **Image Processing**: PIL/Pillow

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd art_generator
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## Usage

1. **Generate Artwork**:
   - Visit the home page
   - Optionally provide a text prompt to guide generation
   - Optionally specify a seed value for reproducible results
   - Click "Generate Art" to create your artwork

2. **Browse Gallery**:
   - Visit the gallery page to see all generated artworks
   - View details like seed values, prompts, and creation dates

3. **Manage Account** (if authenticated):
   - Your generated artworks will be associated with your account
   - Access additional features if implemented

## Project Structure

```
art_generator/
├── art_project/          # Django project settings
├── art_app/             # Main Django application
│   ├── models.py        # Database models
│   ├── views.py         # Application logic
│   ├── urls.py          # URL routing
│   └── admin.py         # Admin interface configuration
├── diffusion_model/     # AI model implementation
│   └── diffusion.py     # Diffusion model code
├── templates/           # HTML templates
│   ├── home.html        # Main generation interface
│   └── gallery.html     # Artwork gallery
├── static/              # Static files (CSS, JS, images)
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```
# Installation Guide for AI Art Generator

## Requirements

### Software Requirements
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)

### Hardware Requirements
- Minimum 4GB RAM (8GB recommended)
- At least 1GB free disk space
- CPU (GPU optional but not required for this simplified implementation)

### Python Package Requirements

Create a `requirements.txt` file with the following content:

```txt
Django==4.2.7
torch==2.0.1
torchvision==0.15.2
Pillow==10.0.1
numpy==1.24.3
```

## Installation Steps

### Step 1: Clone or Create Project Directory

If you have the code in a repository:
```bash
git clone <repository-url>
cd art_generator
```

Or create the directory structure manually:
```bash
mkdir art_generator
cd art_generator
```

### Step 2: Set Up Virtual Environment

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

Create a `requirements.txt` file in your project directory with the content above, then run:

```bash
pip install -r requirements.txt
```

Alternatively, install packages individually:
```bash
pip install Django==4.2.7
pip install torch==2.0.1 torchvision==0.15.2
pip install Pillow==10.0.1
pip install numpy==1.24.3
```

### Step 4: Set Up Django Project

If you haven't already created the project structure:

```bash
django-admin startproject art_project .
python manage.py startapp art_app
```

Create the necessary directories:
```bash
mkdir -p diffusion_model templates static
```

### Step 5: Create Project Files

Create the following files with the content provided in the previous implementation:

1. `diffusion_model/diffusion.py` - The diffusion model implementation
2. `art_app/models.py` - Database models
3. `art_app/views.py` - Application views
4. `art_app/urls.py` - URL routing for the app
5. `templates/home.html` - Main page template
6. `templates/gallery.html` - Gallery template

Update the main URLs file `art_project/urls.py` to include the app URLs.

### Step 6: Configure Django Settings

Update `art_project/settings.py` to include:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'art_app',  # Add this line
]

# Add at the bottom of the file
import os
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Add this line
        'APP_DIRS': True,
        # ... other settings
    },
]
```

### Step 7: Set Up Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 8: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### Step 9: Run the Development Server

```bash
python manage.py runserver
```

### Step 10: Access the Application

Open your web browser and go to:
- Main application: http://localhost:8000
- Admin interface: http://localhost:8000/admin (if you created a superuser)

## Troubleshooting Common Issues

### Issue: "ModuleNotFoundError" for Django
**Solution:** Ensure your virtual environment is activated and Django is installed:
```bash
pip install Django==4.2.7
```

### Issue: "ModuleNotFoundError" for torch
**Solution:** Install PyTorch with the correct version:
```bash
pip install torch==2.0.1 torchvision==0.15.2
```

### Issue: "TemplateDoesNotExist" error
**Solution:** Check your TEMPLATES setting in settings.py and ensure templates directory exists.

### Issue: "CSRF verification failed"
**Solution:** Add CSRF token to your AJAX requests or configure Django settings appropriately.

### Issue: Slow image generation
**Solution:** This is expected with the CPU implementation. For better performance, consider:
1. Using a GPU-enabled PyTorch version
2. Reducing image size in the diffusion model settings
3. Implementing caching

## Verifying Installation

To verify everything is installed correctly, run:

```bash
python manage.py check
```

This should output: "System check identified no issues (0 silenced)."

## Production Deployment Notes

For production deployment, you should:

1. Set `DEBUG = False` in settings.py
2. Set up a proper database (PostgreSQL recommended)
3. Configure a production web server (e.g., Gunicorn with Nginx)
4. Set up static file serving
5. Implement proper security measures

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Pillow Documentation](https://pillow.readthedocs.io/)

Your AI Art Generator should now be ready to use!
## Customization

### Model Parameters

You can adjust the diffusion model parameters in `diffusion_model/diffusion.py`:

- `image_size`: Output image dimensions (default: 128x128)
- `timesteps`: Number of diffusion steps (default: 100)
- Generation steps in the `generate()` method

### Styling

Modify the CSS in the HTML templates or add static CSS files to customize the appearance.

### Database

By default, the project uses SQLite. To use another database, update the `DATABASES` setting in `art_project/settings.py`.

## Performance Considerations

- The current implementation uses a CPU-based simplified diffusion model
- For faster generation, consider:
  - Using a GPU-accelerated PyTorch installation
  - Implementing a more efficient model architecture
  - Adding caching mechanisms
  - Using background task processing (e.g., Celery)

## Limitations

- The current diffusion model is simplified for demonstration purposes
- Image resolution is limited to 128x128 pixels in the default implementation
- Generation may take several seconds on CPU

## Future Enhancements

- Integration with more advanced models (e.g., Stable Diffusion)
- Higher resolution output
- Style transfer capabilities
- Image editing and manipulation features
- Social features (sharing, commenting, liking)
- Advanced user profiles and collections

## Troubleshooting

### Common Issues

1. **Dependency conflicts**:
   - Ensure you're using a virtual environment
   - Check Python version compatibility

2. **Database errors**:
   - Run `python manage.py migrate` to apply migrations

3. **Image generation errors**:
   - Verify all dependencies are installed correctly
   - Check available memory

### Getting Help

If you encounter issues not covered here, please check:
- Django documentation: https://docs.djangoproject.com/
- PyTorch documentation: https://pytorch.org/docs/

## License

This project is provided for educational purposes. Please check the license terms of any external models or libraries you integrate.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
