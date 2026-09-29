from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register, name='register'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('add-food/', views.add_food, name='add_food'),

    path('edit-food/<int:id>/', views.edit_food, name='edit_food'),

    path('delete-food/<int:id>/', views.delete_food, name='delete_food'),
]