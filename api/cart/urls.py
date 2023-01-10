from django.urls import path
from .views import cart_detail

app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='detail'),
]
