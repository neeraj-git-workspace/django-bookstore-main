from django.urls import path
from django.conf.urls.static import static
from bookstore import settings
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about_detail, name='about_detail'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
