from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name= 'home'),
    path('products/', views.products, name= 'products'),
    path('customer/<str:pk>/', views.customer, name = 'customer'),
    path('order/<str:pk>/', views.Create_order, name= 'order'),
    path('update/<str:pk>/', views.update_form, name= 'update'),

    path('delete/<str:pk>/', views.delete_form, name= 'delete')
]