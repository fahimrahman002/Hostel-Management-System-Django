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

class MealRecord(models.Model):
    hostel=models.ForeignKey(Hostel,on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    date=models.DateField(blank=True,null=True)
    meal_lunch=models.BooleanField(default=True)
    meal_dinner=models.BooleanField(default=True)
    
class BazarDetail(models.Model):
    hostel=models.ForeignKey(Hostel,on_delete=models.CASCADE)
    member=models.ForeignKey(Member,on_delete=models.SET_NULL,blank=True,null=True)
    date=models.DateField(blank=True,null=True)
    details=models.TextField(default="", blank=True, null=True)
    expense=models.IntegerField(default=0)
    
