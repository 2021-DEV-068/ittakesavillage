from typing import Any, Dict

from django.views.generic import TemplateView

from website.models.choices import Speciality


class SpecialityInfoView(TemplateView):
    template_name = "website/parent/info/speciality.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['specialities'] = Speciality.values
        return context



