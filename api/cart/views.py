from django.shortcuts import render


def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
