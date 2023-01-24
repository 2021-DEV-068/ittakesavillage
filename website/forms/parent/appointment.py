from django import forms
from django.utils.translation import gettext_lazy as _

from website.models.choices import Speciality


class AppointmentForm(forms.Form):
    speciality = forms.ChoiceField(
        choices=Speciality.availability_choices(),
        required=True
    )
    first_appointment = forms.BooleanField(label=_('First appointment'))
    slot = forms.DateTimeField(required=True)
