from django import forms

from website.models.choices import Speciality, City


class SearchCaregiverForm(forms.Form):
    speciality = forms.ChoiceField(choices=Speciality.choices, required=False)
    city = forms.ChoiceField(choices=City.choices, required=False)
