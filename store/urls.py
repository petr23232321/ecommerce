from django.urls import path, include
from store.views import store, product_detail, search, submit_review


app_name='product'
urlpatterns = [
    path('', store, name='products'),
    path('category/<slug:category_slug>/', store, name='category_slug'),
    path('category/<slug:category_slug>/<slug:product_slug>/', product_detail, name='product_detail'),
    path('search/', search, name='search'),
    path('submit_review/<int:product_id>', submit_review, name='submit_review'),


]