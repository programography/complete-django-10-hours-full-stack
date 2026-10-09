from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MyAllTodos(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank = True)
    title = models.CharField(max_length=150)
    priority = models.CharField(max_length=50)
    todo_pic = models.ImageField(upload_to="todo_images") 
    description = models.TextField()
    is_deleted = models.BooleanField(default = False)
    craeted_at = models.DateTimeField(auto_now=False, auto_now_add=True)