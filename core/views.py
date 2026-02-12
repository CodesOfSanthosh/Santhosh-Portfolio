from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project, Certification
from .forms import ContactForm

def index(request):
    skills = Skill.objects.filter(is_active=True)
    projects = Project.objects.all().order_by('-created_at')
    
    # Manually process tech stacks
    for project in projects:
        if project.tech_stack:
            project.tech_stack_display = [t.strip() for t in project.tech_stack.split(',') if t.strip()]
        else:
            project.tech_stack_display = []
            
    certifications = Certification.objects.all().order_by('-date_issued')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
    else:
        form = ContactForm()
    
    context = {
        'skills': skills,
        'projects': projects,
        'certifications': certifications,
        'form': form,
    }
    return render(request, 'core/index.html', context)
