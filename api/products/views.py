from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Category, Product
from getnet import Client

client = Client(seller_id='SELLER_ID', client_id='SUA_CHAVE_CLIENTE', client_secret='SUA_CHAVE_SECRETA')
client.auth()


class ProductDetailView(DetailView):
    queryset = Product.available.all()


class ProductListView(ListView):
    category = None
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.available.all()

        category_slug = self.kwargs.get('slug')
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        return context
    
class ProductBuyView(DetailView):
    def buy(request, product_id):
        if request.method == 'POST':
            product = Product.objects.get(id=product_id)
            if product.stock > 0:
                # Obtenha os dados do cartão de crédito do formulário
                card_number = request.POST.get('card_number')
                card_holder_name = request.POST.get('card_holder_name')
                card_expiration_month = request.POST.get('card_expiration_month')
                card_expiration_year = request.POST.get('card_expiration_year')
                Product.stock -= 1
