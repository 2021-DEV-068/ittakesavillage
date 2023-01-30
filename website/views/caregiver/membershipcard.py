from django.views.generic import TemplateView
# from django.shortcuts import render
from django.urls import reverse


class membershipCardView():
    template_name = "website/caregiver/membershipcard.html"
    # render('caregiver/membershipcard.html')
    reverse("caregiver:membershipcard")
    # template_name = "website/caregiver/signup.html"
    # form_class = SignUpForm
    # success_message = _("We will proceed your request.")

    # def form_valid(self, form):
    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse("caregiver:home")



    
