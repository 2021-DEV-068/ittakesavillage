from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class membershipCardView():
    render('caregiver/membershipcard.html')
    # template_name = "website/caregiver/signup.html"
    # form_class = SignUpForm
    # success_message = _("We will proceed your request.")

    # def form_valid(self, form):
    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse("caregiver:home")
