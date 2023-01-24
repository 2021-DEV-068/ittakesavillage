import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from website.forms.parent.appointment import AppointmentForm
from website.models.appointment import Appointment
from website.models.caregiver import Caregiver


class AppointmentCreateView(LoginRequiredMixin, FormView, SuccessMessageMixin):
    template_name = "website/parent/caregiver/detail.html"

    form_class = AppointmentForm

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        Appointment(
            specialist=Caregiver.objects.get(pk=self.kwargs['pk']),
            parent=self.request.user.parent,
            from_time=form.cleaned_data['slot'],
            duration=datetime.timedelta(minutes=30),
        ).save()

        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return _('Booked')

    def get_success_url(self):
        return reverse("specialist_detail", kwargs={"pk": self.kwargs['pk']})
