import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Check if superuser already exists
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='admin123'  # Change this to a secure password
    )
    print("Superuser created successfully!")
    print("Username: admin")
    print("Password: admin123")
    print("IMPORTANT: Change this password after first login!")
else:
    print("Superuser already exists.")
