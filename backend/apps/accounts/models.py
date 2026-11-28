from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employer', 'Employer'),
        ('candidate', 'Candidate'),
    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='candidate')
    
    email = models.EmailField(unique="True")
    
    phone = models.CharField(max_length=20, blank="true", null="true")
    
    profile_image = models.ImageField(upload_to='users/profile', blank=True, null=True)
    
    created_at = models.DateTimeField( auto_now=True)
    
    updated_at = models.DateField( auto_now=True)
    
    
    
    
