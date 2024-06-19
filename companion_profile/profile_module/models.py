from django.db import models

# Create your models here.

class Companion_profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='photos/',blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True)
    linked_in = models.URLField(max_length=255, blank=True, null=True)
    git_hub = models.URLField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15)
    resume_file = models.FileField(upload_to='resumes/', blank=True, null=True)
    domain = models.CharField(max_length=100, blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    deleted = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

