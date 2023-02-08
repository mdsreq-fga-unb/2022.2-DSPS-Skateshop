from django.urls import path

from .views import LoginPage, CadastroPage

app_name = 'users'

urlpatterns = [
    path('login/', LoginPage.as_view(), name = 'login'),
    path(r'^cadastro/$', CadastroPage.as_view(), name = 'cadastro'),
]