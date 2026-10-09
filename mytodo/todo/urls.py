from django.urls import path
from todo import views

urlpatterns = [
    path("", views.maintodopage, name = "todo"),
    path("save-new-todo", views.savingtodo, name = "savetodo"),
    path("delete-todo/<int:myid>", views.deletetodo, name = "delete"),
    path("todo-done/<int:todoid>", views.donetodo, name = "donetodo"),
    path("update-todo-now/<int:u_id>", views.updatenow, name = "updatenow"),
    
    # auth
    
    path("login", views.loginhere, name = "login"),
    path("signup", views.signuphere, name = "signup"),
    
    path("sign-up-here", views.signupherenw, name = "here"),
    
    path("logout", views.logoutuser, name = "logout")
]
