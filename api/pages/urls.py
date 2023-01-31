from django.urls import path

from .views import AboutPageView, HomePageView, ContactPageView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact')
]
