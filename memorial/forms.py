from django import forms
from .models import Person, Memory

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        exclude = []