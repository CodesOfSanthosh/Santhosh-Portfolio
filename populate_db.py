import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from core.models import Project, Skill

# Projects Data
projects_data = [
    {
        "title": "Spotify Clone",
        "description": "A clone of the Spotify web player using HTML, CSS, and potentially JavaScript.",
        "tech_stack": "HTML, CSS",
        "github_link": "https://github.com/CodesOfSanthosh/SpotifyClone",
        "live_link": "https://codesofsanthosh.github.io/SpotifyClone/"
    },
    {
        "title": "Responsive HTML CSS Project",
        "description": "A fully responsive website built with raw HTML and CSS.",
        "tech_stack": "HTML, CSS",
        "github_link": "https://github.com/CodesOfSanthosh/responsive-html-css-project",
        "live_link": "https://codesofsanthosh.github.io/responsive-html-css-project/"
    },
    {
        "title": "Responsive Bootstrap Project",
        "description": "A responsive website utilizing the Bootstrap framework.",
        "tech_stack": "Bootstrap, HTML, CSS",
        "github_link": "https://github.com/CodesOfSanthosh/responsive-bootstrap",
        "live_link": "https://codesofsanthosh.github.io/responsive-bootstrap/"
    },
    {
        "title": "React Django Job Portal",
        "description": "A full-stack job portal application built with React and Django.",
        "tech_stack": "React, Django, Python",
        "github_link": "https://github.com/CodesOfSanthosh/react-django-job-portal",
        "live_link": ""
    },
    {
        "title": "Django E-commerce",
        "description": "An e-commerce platform built with Django.",
        "tech_stack": "Django, Python",
        "github_link": "https://github.com/CodesOfSanthosh/django-ecommerce",
        "live_link": ""
    },
    {
        "title": "Blog Django",
        "description": "A blog application built with Django.",
        "tech_stack": "Django, Python",
        "github_link": "https://github.com/CodesOfSanthosh/blog-django",
        "live_link": ""
    }
]

# Skills Data
skills_data = [
    {"name": "HTML", "icon_class": "fab fa-html5", "proficiency": 90},
    {"name": "CSS", "icon_class": "fab fa-css3-alt", "proficiency": 85},
    {"name": "Bootstrap", "icon_class": "fab fa-bootstrap", "proficiency": 80},
    {"name": "React", "icon_class": "fab fa-react", "proficiency": 75},
    {"name": "Django", "icon_class": "fab fa-python", "proficiency": 85}, # FontAwesome doesn't have a specific django icon, using python or generic server
    {"name": "Python", "icon_class": "fab fa-python", "proficiency": 90},
    {"name": "MySQL", "icon_class": "fas fa-database", "proficiency": 70},
    {"name": "Postman", "icon_class": "fas fa-paper-plane", "proficiency": 80}, # Generic icon or specialized one if available
    {"name": "VS Code", "icon_class": "fas fa-code", "proficiency": 95},
    {"name": "SQLite", "icon_class": "fas fa-database", "proficiency": 80},
    {"name": "Git", "icon_class": "fab fa-git-alt", "proficiency": 85},
    {"name": "GitHub", "icon_class": "fab fa-github", "proficiency": 85},
]

def populate():
    print("Populating Projects...")
    for project in projects_data:
        p, created = Project.objects.get_or_create(
            title=project['title'],
            defaults={
                'description': project['description'],
                'tech_stack': project['tech_stack'],
                'github_link': project['github_link'],
                'live_link': project['live_link']
            }
        )
        if created:
            print(f"Created Project: {project['title']}")
        else:
            print(f"Project already exists: {project['title']}")

    print("\nPopulating Skills...")
    for skill in skills_data:
        s, created = Skill.objects.get_or_create(
            name=skill['name'],
            defaults={
                'icon_class': skill['icon_class'],
                'proficiency': skill['proficiency']
            }
        )
        if created:
            print(f"Created Skill: {skill['name']}")
        else:
            print(f"Skill already exists: {skill['name']}")

if __name__ == '__main__':
    populate()
