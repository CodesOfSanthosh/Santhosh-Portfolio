from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, help_text="FontAwesome or DevIcon class", blank=True)
    proficiency = models.IntegerField(help_text="Percentage (0-100)", default=80)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    tech_stack = models.CharField(max_length=200, help_text="Comma separated technologies")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def tech_stack_list(self):
        if not self.tech_stack:
            return []
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuing_authority = models.CharField(max_length=200)
    date_issued = models.DateField()
    certificate_link = models.URLField(blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.issuing_authority}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
