from django.db import models
from django.contrib.auth.models import User


class Hostel(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title}"


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hostel = models.OneToOneField(
        Hostel, on_delete=models.CASCADE, blank=True, null=True)
    admin_privilege = models.BooleanField(default=False)
    about = models.TextField(default="", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
