from django.db import models
from django.core.validators import EmailValidator, RegexValidator
from PIL import Image

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    location = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Image cropping (450x350 as per requirements)
        if self.image:
            img = Image.open(self.image.path)
            
            # Target ratio: 450x350
            target_width, target_height = 450, 350
            
            # Calculate cropping box
            width, height = img.size
            aspect = target_width / target_height
            
            if width / height > aspect:
                new_width = int(height * aspect)
                left = (width - new_width) // 2
                img = img.crop((left, 0, left + new_width, height))
            else:
                new_height = int(width / aspect)
                top = (height - new_height) // 2
                img = img.crop((0, top, width, top + new_height))
            
            # Resize and save
            img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
            img.save(self.image.path)
    
    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='clients/')
    company = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.designation}"

class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    mobile_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Enter a valid phone number"
            )
        ]
    )
    city = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.full_name} - {self.email}"

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.email