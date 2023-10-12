from django.urls import path
from django.conf.urls.static import static

from bookstore import settings
from . import views

app_name = 'contact'

urlpatterns = [
                  path('map/', views.contact_detail, name='contact_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
