from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import FormView   
from django.urls import reverse_lazy
from django.core.mail import send_mail

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("contact:submitted")
    
    def form_valid(self, form):
        first_name = form.cleaned_data.get("first_name").capitalize()
        last_name = form.cleaned_data.get("last_name").capitalize()
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        
        send_mail(
            subject=f"New Contact Form Submission from {first_name} {last_name}",
            message=message,
            from_email=email,
            recipient_list=["hasmeedcoder@@gmail.com", email],
        )
        form.save()
        return super().form_valid(form)
    
class ContactSubmittedView(FormView):
    template_name = "contact_submitted.html"