import uuid
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.username

class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20,null=True)
    computers=models.IntegerField(null=True)
    hasCompters=models.BooleanField(null=True)

    def __str__(self) -> str:
        return self.name

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    bookDate=models.DateTimeField( auto_now_add=True)
    date=models.DateField(null=True)
    startTime=models.TimeField(null=True)
    endTime=models.TimeField(null=True)
    purpose=models.CharField( max_length=50,default='Studying',)
    coins=models.FloatField(default=0)
    points=models.FloatField(default=0)
    computers=models.IntegerField(default=0)
    description=models.CharField(max_length=100,null=True)
    isUsed= models.BooleanField(default=False, null=True)
    duration=models.FloatField(default=0)
    referenceNo=models.CharField(max_length=8,blank=True,unique=True, default=uuid.uuid1)
    officeName=models.CharField(max_length=50,null=True)
    status=models.CharField(max_length=20,null=True, default='Booked')
    user=models.CharField(max_length=50,null=True)
    venue=models.ForeignKey(Venue,related_name='venue',to_field='id',on_delete=models.CASCADE)
    user_id=models.IntegerField(default=0,null=True)
    def __str__(self) -> str:
        return f"REF NO:{self.referenceNo}"

class Attendee(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,null=True)
    user_id=models.IntegerField(null=True)
    booking=models.ForeignKey(Booking,related_name='attendees',on_delete=models.CASCADE,null=True)   
    
    def __str__(self) -> str:
        return f"{self.name}"    

