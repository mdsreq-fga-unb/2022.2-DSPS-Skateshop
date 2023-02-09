from django.urls import path

from .views import AboutPageView, HomePageView, ContactPageView, FaqPageView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('faq/', FaqPageView.as_view(), name='faq')
]
