from django.urls import path
from django.conf.urls.static import static
from bookstore import settings
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("search_ajax/", views.search, name="search_ajax"),
    path('<int:id>/<slug>/', views.product_detail, name='product_detail'),
    path('<category_slug>/', views.product_list, name='product_list_by_category')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
