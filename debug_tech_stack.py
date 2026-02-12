import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import Project

projects = Project.objects.all()
print(f"Total projects: {projects.count()}")

for p in projects:
    print(f"Project: {p.title}")
    print(f"Original tech_stack: '{p.tech_stack}'")
    print(f"Split list: {p.tech_stack_list}")
    print("-" * 20)
