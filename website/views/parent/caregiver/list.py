import datetime

from django_filters.views import FilterView

from website.filters.parent.caregiver import CaregiverFilter
from website.models.caregiver import Caregiver


class CaregiverListView(FilterView):
    template_name = "website/parent/caregiver/list.html"
    model = Caregiver
    filterset_class = CaregiverFilter

    def get_queryset(self):
        return Caregiver.objects.with_consultation_slots()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context

