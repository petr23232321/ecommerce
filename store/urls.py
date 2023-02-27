from django.urls import path, include
from store.views import store, product_detail


app_name='product'
urlpatterns = [
    path('', store, name='products'),
    path('<slug:category_slug>/', store, name='category_slug'),
    path('<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),

]