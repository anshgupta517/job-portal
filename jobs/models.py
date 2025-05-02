from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to="applicant_profile_images", null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=15, null=True, blank=True)
    
    def __str__(self):
        return self.user.username

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to="company_profile_images", null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    type = models.CharField(max_length=15, null=True, blank=True)
    status = models.CharField(max_length=15, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.company_name

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    creation_date = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to="job_images", null=True, blank=True)
    
    def __str__(self):
        return self.title

class Application(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resumes")
    apply_date = models.DateField()
    
    def __str__(self):
        return f"{self.applicant.user.username} applied for {self.job.title}"
