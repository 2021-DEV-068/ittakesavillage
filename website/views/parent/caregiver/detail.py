import datetime

from django.views.generic import DetailView

from website.forms.parent.appointment import AppointmentForm
from website.models.caregiver import Caregiver


class CaregiverDetailView(DetailView):
    template_name = "website/parent/caregiver/detail.html"
    model = Caregiver

    context_object_name = "caregiver"

    def get_queryset(self):
        return Caregiver.objects.with_consultation_slots()

    def get_context_data(self, **kwargs):
        return {
            'slots': [],
            'days': [datetime.date.today() + datetime.timedelta(days=i) for i in range(0, 7)],
            'form': AppointmentForm(),
            **super().get_context_data(**kwargs),
        }
