from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class PersonalProfile(models.Model):
    username = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    phone_no = PhoneNumberField(blank=True, unique=True)
    additional_info = models.TextField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "personal_profile"

    def get_absolute_url(self):
        return reverse("personalprofile:info", args=[self.id])

    def __str__(self):
        return self.username
