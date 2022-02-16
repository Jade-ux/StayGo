from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
]
