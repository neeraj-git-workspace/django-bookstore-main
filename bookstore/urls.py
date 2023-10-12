from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from shop.views import ProductsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('about/', include('about.urls')),
    path('', include('shop.urls', namespace="shop")),
    path('accounts/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('', ProductsView.as_view(), name="products"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
