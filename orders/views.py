import time
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from carts.models import Cart
# Create your views here.
from .models import Order


def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("cart"))

    new_order, created = Order.objects.get_or_create(cart=cart)
    if created:
        # Assign a user to the order
        new_order.order_id = str(time.time())
        new_order.save()
    # Assign address to the order
    # Run credit card
    if new_order.status == "Finished":
        cart.delete()
        del request.session['cart_id']
        del request.session['items_count']
        return HttpResponseRedirect(reverse("cart"))
    context = {}
    template = "products/home.html"
    return render(request, template, context)