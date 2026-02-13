import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import Skill, Project, Certification

# Export data to JSON
data = {
    'skills': [],
    'projects': [],
    'certifications': []
}

# Get skills
for skill in Skill.objects.filter(is_active=True):
    data['skills'].append({
        'name': skill.name,
        'icon_class': skill.icon_class
    })

# Get projects
for project in Project.objects.all().order_by('-created_at'):
    tech_stack = [t.strip() for t in project.tech_stack.split(',') if t.strip()] if project.tech_stack else []
    data['projects'].append({
        'title': project.title,
        'description': project.description,
        'tech_stack': tech_stack,
        'github_link': project.github_link or '',
        'live_link': project.live_link or '',
        'image_url': project.image.url if project.image else ''
    })

# Get certifications
for cert in Certification.objects.all().order_by('-date_issued'):
    data['certifications'].append({
        'title': cert.title,
        'issuing_authority': cert.issuing_authority,
        'certificate_link': cert.certificate_link or ''
    })

# Save to JSON file
with open('portfolio_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Data exported to portfolio_data.json")
print(f"   Skills: {len(data['skills'])}")
print(f"   Projects: {len(data['projects'])}")
print(f"   Certifications: {len(data['certifications'])}")
