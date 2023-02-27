from django.urls import path

from carts import views
from carts.views import cart
app_name='cart'
urlpatterns =[
    path('', cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
]