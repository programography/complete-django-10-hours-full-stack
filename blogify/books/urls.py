from django.urls import path
from books import views

urlpatterns = [
   path("python-book", views.pythonbook, name = "python"),
   path("java-book", views.javabook, name = "java")
]