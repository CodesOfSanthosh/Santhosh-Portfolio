"""
WSGI wrapper for Vercel deployment
This file is used by Vercel to serve the Django application
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Get the WSGI application
application = get_wsgi_application()

# Vercel serverless function handler
app = application
