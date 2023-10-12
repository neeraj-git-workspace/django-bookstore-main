import random

from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView

from cart.forms import CartAddProductForm
from .models import Category, Product, Myrating


class ProductsView(ListView):
    model = Product
    paginate_by = 10
    context_object_name = 'lists'
    template_name = 'shop/list.html'
    ordering = ['name']


# def callajax(request):
#     if request.method == 'POST':
#         response_json = request.POST
#         response_json = json.dumps(response_json)
#         data = json.loads(response_json)
#         counter = int(data['counter'])
#         obj = Product.objects.all()[counter:][:20]
#         data = serializers.serialize('json', obj)
#         data = {'data': data}
#     return JsonResponse(data, safe=False)


# List
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    all_product = Product.objects.filter(available=True)
    possible_ids = random.choices(list(all_product.values_list('id', flat=True)), k=10)
    products = all_product.filter(pk__in=possible_ids)

    search_term = ''
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        all_product = Product.objects.filter(category=category)
        possible_ids = random.choices(list(all_product.values_list('id', flat=True)), k=10)
        products = all_product.filter(pk__in=possible_ids)

    if 'search' in request.GET:
        search_term = request.GET['search']
        products = Product.objects.filter(name__icontains=search_term)[:10:1]
        if products:
            messages.success(request, 'You searched ' + search_term)
        else:
            messages.success(request, 'Book not found')

    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(title__icontains=query)).distinct()
        return render(request, 'shop/list.html', {'products': products})

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'search_term': search_term
    }
    return render(request, 'shop/list.html', context)


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


@csrf_exempt
def search(request):
    if request.method == "POST" and is_ajax(request=request):
        message = request.POST.get("message", None)
        # message = request.POST['send']
        print(message)
        products = Product.objects.filter(name__icontains=message)[:10:1]
        if products:
            messages.success(request, 'You searched ' + message)
        else:
            messages.success(request, 'Book not found')
        context = {
            'products': products,
            'search_term': message
        }
        return render(request, 'shop/list.html', context)
    else:
        message = "Please check the POST call"
    return HttpResponse(message)


# detail
def product_detail(request, id, slug):
    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    cart_product_form = CartAddProductForm()

    # rating
    if request.method == "POST":
        rate = request.POST['rating']
        ratingObject = Myrating()
        ratingObject.user = request.user
        ratingObject.product = product
        ratingObject.rating = rate
        ratingObject.save()
        messages.success(request, "Your Rating is submited ")
        return redirect('shop:product_list')

    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'shop/detail.html', context)