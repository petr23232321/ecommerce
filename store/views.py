from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from store.models import Products, Category
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from carts.views import _cart_id

def home(request):
    products = Products.objects.filter(is_available=True)
    paginator = Paginator(products, 4)
    context = {
        'products': products,
    }
    return render(request, 'store/index.html', context)

def store(request, category_slug=None):
    if category_slug:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Products.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Products.objects.filter(is_available=True)
        product_count = products.count()
    per_page = 2
    paginator = Paginator(products, per_page)
    page = request.GET.get('page')
    products_paginator = paginator.get_page(page)

    context = {
        'products': products_paginator,
        'product_count': product_count,
        'categories': Category.objects.all(),
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    single_product = Products.objects.get(category__slug=category_slug, slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Products.objects.order_by('-create_date').filter(description__icontains=keyword)
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


