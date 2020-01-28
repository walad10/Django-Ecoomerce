"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from products.views import search, all, home, single
from carts.views import view, update_cart
from django.conf.urls.static import static
admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^s/$', search, name='search'),
    path('', home, name='home'),
    path('products/', all, name='products'),
    re_path(r'^products/(?P<slug>[\w-]+)/$', single, name='single_product'),
    re_path(r'cart/$', view, name='cart'),
    re_path(r'^cart/(?P<slug>[\w-]+)/$', update_cart, name='update_cart'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
