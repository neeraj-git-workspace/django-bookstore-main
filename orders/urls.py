from django.urls import path
from django.conf.urls.static import static
from bookstore import settings
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
