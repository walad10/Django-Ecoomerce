from django.db import models
from products.models import Product

# Create your models here.


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', null=True, blank=True,  on_delete=models.PROTECT)
    line_total = models.DecimalField(default=1000, max_digits=10000, decimal_places=2)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
    notes = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.title


class Cart(models.Model):
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "car id: %s" % (self.id)



