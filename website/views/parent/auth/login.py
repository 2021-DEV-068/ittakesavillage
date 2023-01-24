from django.contrib.auth.views import LoginView
from django.urls import reverse


class LoginClientView(LoginView):
    template_name = "website/parent/auth/login.html"

    def get_default_redirect_url(self):
        return reverse("parent:caregiver_list")
