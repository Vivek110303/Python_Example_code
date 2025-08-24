from app.models import Contact
from django import forms

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = [('name','lastname', 'email', 'content')]