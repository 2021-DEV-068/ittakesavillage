from django import forms

from website.models.choices import Speciality


class SignUpForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    city = forms.CharField(required=True)
    specialities = forms.MultipleChoiceField(required=True, choices=Speciality.choices)
    inami = forms.CharField(required=False)
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": "5"}))

