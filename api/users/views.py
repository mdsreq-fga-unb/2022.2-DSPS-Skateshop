from .forms import CustomUserCreationForm

from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("pages:home")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    template_name = "cadastro.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    template_name = "logout.html"
