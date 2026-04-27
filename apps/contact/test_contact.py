from django.urls import reverse
import pytest
from apps.contact.forms import ContactForm
from django import forms
from apps.contact.models import Contact
from mixer.backend.django import mixer
from django.db import models
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware

from apps.contact.views import ContactFormView

form_data = [
    ("Hameed", "Yusuf", "hasmeedcoder@gmail.com", "Testing Message", True, True),
    ("Hameed", "Yusuf", "hasmeedcodergmail.com", "Testing Message", True, False),
    ("Hameed", "Yusuf", "hasmeedcoder@gmail", "Testing Message", True, False),
    ("Hameed", "", "hasmeedcoder@gmail", "Testing Message", True, False),
    ("", "Yusuf", "hasmeedcoder@gmail", "Testing Message", True, False),
    ("Hameed", "Yusuf", "hasmeedcoder@gmail.com", "Testing Message", False, True),
]


@pytest.fixture(scope="function")
def contact_data():
    return {
        "first_name": "Hameed",
        "last_name": "Yusuf",
        "email": "hasmeedcoder@gmail.com",
        "message": " Testing Message",
        "captcha": True,
    }


@pytest.fixture(name="random_contact", scope="function")
def random_contact():
    return mixer.blend(Contact)


class TestContactFormRegistration:
    fields = ["first_name", "last_name", "email", "message", "captcha", "validity"]

    @pytest.mark.parametrize(argnames=fields, argvalues=form_data)
    def test_contact_form_fields(
        self, first_name, last_name, email, message, captcha, validity
    ):
        class CustomContactForm(ContactForm):
            captcha = forms.BooleanField(required=False, widget=forms.HiddenInput)

            def clean_captcha(self):
                return True

        form = CustomContactForm(
            data={
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "message": message,
                "captcha": captcha,
                "validity": validity,
            }
        )

        assert (
            form.is_valid() is validity
        ), "Assert valid form submission for input variation"


@pytest.mark.django_db(reset_sequences=True)
class TestContactModel:
    def test_single_contact_save(self, random_contact):
        assert random_contact.pk == 1

    def test_multiple_contacts(self):
        contacts = mixer.cycle(10).blend(Contact)
        assert Contact.objects.count() == 10
        assert contacts[5].pk == 6

    def test_delete_contact(self):
        contacts = mixer.cycle(5).blend(Contact)
        assert Contact.objects.count() == 5
        contacts[2].delete()
        assert Contact.objects.count() == 4

    def test_first_name_is_charfield(self, random_contact):
        first_name = random_contact._meta.get_field("first_name")
        assert isinstance(first_name, models.CharField)

    def test_fullname(self):
        contact = mixer.blend(Contact)
        contact.first_name = "Hameed"
        contact.last_name = "Yusuf"
        assert contact.full_name == "Hameed Yusuf"


class TestContactURL:
    def test_contact(self):
        path = reverse("contact:contact")
        assert path and path == "/contact/"

    def test_submitted_contact(self):
        path = reverse("contact:submitted")
        assert path and path == "/contact/submitted/"


@pytest.mark.django_db(reset_sequences=True)
class TestContactForm:
    def test_contact_form(self, rf, contact_data):
        path = reverse("contact:contact")
        request = rf.post(path, contact_data)
        request.user = AnonymousUser
        response = ContactFormView.as_view()(request, contact_data)
        assert Contact.objects.count() == 1
        assert response.status_code == 302
