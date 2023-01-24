from django.urls import path

from website.views.caregiver.home import HomeView
from website.views.caregiver.signup import SignUpView

app_name = 'website'
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("signup", SignUpView.as_view(), name="signup"),
]
