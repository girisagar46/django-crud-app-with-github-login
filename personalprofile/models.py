from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class PersonalProfile(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    description  = models.TextField(null=True)
    phone_no = PhoneNumberField(blank=True, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)


    def get_absolute_url(self):
        return reverse('personalprofile:info', args=[self.id])
    

    class Meta:
        ordering = ['-published_at']
    
    
    def __str__(self):
        return self.name
