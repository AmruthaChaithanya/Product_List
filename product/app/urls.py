from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name= 'home'),
    path('index/',views.products, name= 'index'),
    path('add/',views.add, name= 'add'),
    path('edit/<int:product_id>/',views.edit, name= 'edit'),
    path('delete/<int:product_id>/',views.delete, name= 'delete'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('apilist',views.product_list, name='apilist'),
    path('apicreate',views.product_create, name='apicreate'),
]