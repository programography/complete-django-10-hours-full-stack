from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("about", views.about, name = "about"),
    path("contact-us", views.contactus, name = "contactus"),
    path("services", views.services, name = "services"),
    path("save-contact-us-data", views.saving_data, name = "savedata"),
    path("our-queries", views.our_contact_forms, name = "our_contact_forms"),
    path("delete-query/<int:x>", views.deletequery, name = "dltq"),
    path("update-contact-us-data/<int:myid>", views.updatedata, name = "updated")
]

