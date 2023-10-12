from django.urls import path
from django.conf.urls.static import static
from bookstore import settings
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<product_id>/', views.cart_add, name='cart_add'),
    path('remove/<product_id>/', views.cart_remove, name='cart_remove'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
