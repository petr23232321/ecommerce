from django.urls import path, include
from store.views import store, product_detail, search


app_name='product'
urlpatterns = [
    path('', store, name='products'),
    path('category/<slug:category_slug>/', store, name='category_slug'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('search/', search, name='search'),


]