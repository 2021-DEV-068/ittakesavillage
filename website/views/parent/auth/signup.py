from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView

from website.models.parent import Parent


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    field_order = ['first_name', 'last_name']


class SignupView(CreateView):
    template_name = "website/parent/auth/signup.html"
    model = User
    form_class = SignUpForm

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()

        Parent(user=self.object).save()

        return response

    def get_success_url(self):
        return reverse('parent:home')
