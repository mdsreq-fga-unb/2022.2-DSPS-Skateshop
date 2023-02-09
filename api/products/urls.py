from django.urls import path

from .views import ProductDetailView, ProductListView, ProductBuyView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='detail'),
    path('category/<slug:slug>', ProductListView.as_view(), name='list_by_category'),
    path('/comprar/', ProductBuyView.as_view(), name='comprar')
]
