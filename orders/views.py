from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart

# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST'