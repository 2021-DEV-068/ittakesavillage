from django.urls import path

from website.views.parent.appointment.create import AppointmentCreateView
from website.views.parent.home import HomeView
from website.views.parent.auth.login import LoginClientView
from website.views.parent.auth.logout import LogoutClientView
from website.views.parent.auth.signup import SignupView
from website.views.parent.caregiver.detail import CaregiverDetailView
from website.views.parent.caregiver.list import CaregiverListView
from website.views.parent.info.speciality import SpecialityInfoView

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginClientView.as_view(), name="login"),
    path('logout/', LogoutClientView.as_view(), name="logout"),
    path('signup/', SignupView.as_view(), name="signup"),
    path('caregiver/', CaregiverListView.as_view(), name='caregiver_list'),
    path('caregiver/<int:pk>/', CaregiverDetailView.as_view(), name="caregiver_detail"),
    path('appointment/<int:pk>/', AppointmentCreateView.as_view(), name="appointment_create"),
    path('info/speciality/', SpecialityInfoView.as_view(), name="info_speciality"),
]
