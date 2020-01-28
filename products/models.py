from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()
    sales_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

    def get_absolute_url(self):
        return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def colors(self):
        return self.all().filter(category='color')

    def sizes(self):
        return self.all().filter(category='size')


VAR_CATEGORIES = (
    ('size', 'size'),
    ('color', 'color'),
    ('package', 'package'),
)


class Variation(models.Model):
    product = models.ForeignKey(Product,  on_delete=models.PROTECT)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='color')
    title = models.CharField(max_length=120)
    image = models.ForeignKey(ProductImage, null=True, blank=True, on_delete=models.PROTECT)
    price = models.DecimalField(blank=True, null=True, max_digits=100000, decimal_places=2)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    objects = VariationManager()

    def __str__(self):
        return self.title

