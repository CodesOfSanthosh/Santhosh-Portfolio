from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if one does not exist'

    def handle(self, *args, **options):
        User = get_user_model()
        
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@portfolio.com',
                password='Portfolio@2026'  # Change this after first login!
            )
            self.stdout.write(self.style.SUCCESS('✅ Superuser created successfully!'))
            self.stdout.write(self.style.WARNING('Username: admin'))
            self.stdout.write(self.style.WARNING('Password: Portfolio@2026'))
            self.stdout.write(self.style.ERROR('⚠️  IMPORTANT: Change this password after first login!'))
        else:
            self.stdout.write(self.style.SUCCESS('✅ Superuser already exists.'))
