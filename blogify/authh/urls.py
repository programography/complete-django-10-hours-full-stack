from django.urls import path
from authh import views

urlpatterns = [
    path("sign-up", views.signup, name = "signup"),
    path("login", views.login_page, name = "login"),
    path("user-logout", views.userlogout, name = "logout")
]
