from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class membershipCardView(SuccessMessageMixin):
    template_name = "website/caregiver/membershipcard.html"
    success_message = _("We will proceed your request.")
    def get_success_url(self):
        return reverse("caregiver:membershipcard")
