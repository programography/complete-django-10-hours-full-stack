from django.db import models

# Create your models here.
 
class ContactUsModel(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254) 
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    address = models.TextField()
    message = models.TextField()