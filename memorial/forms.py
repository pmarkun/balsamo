from django import forms
from .models import Person, Memory
import datetime

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['user']

    birth = forms.DateField(
        widget=forms.DateInput(
            format=('%d/%m/%Y',),
            attrs={
                "type" : "date",
                "class": "",
            }
        ),
        #input_formats='%d/%m/%Y',

        #initial=datetime.datetime.today,
        # required=False,
        # label=_("birth date"),
    )

    death = forms.DateField(
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                "type" : "date",
                "class": "",
            }
        ),
        initial=datetime.datetime.today,
        #input_formats='%d/%m/%Y',

        # required=False,
        # label=_("birth date"),
    )


class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        exclude = ['user']
        widgets = {
            'person': forms.HiddenInput(),
        }


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Nome')
    last_name = forms.CharField(max_length=30, label='Sobrenome')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()