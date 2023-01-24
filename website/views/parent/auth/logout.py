from django.contrib.auth.views import LogoutView
from django.urls import reverse


class LogoutClientView(LogoutView):

    def get_default_redirect_url(self):
        return reverse("parent:home")
