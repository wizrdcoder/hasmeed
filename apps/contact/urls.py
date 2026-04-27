from django.urls import path

from apps.contact.views import ContactFormView, ContactSubmittedView



app_name = "contact"

urlpatterns = [
    path("", ContactFormView.as_view(), name="contact"),
    path("submitted/", ContactSubmittedView.as_view(), name="submitted"),
]
