from django.urls import path
from . import views

urlpatterns = [
    path('', views.vans, name='vans'),
    path('<int:van_id>/', views.van_detail, name='van_detail'),
]
