from django.urls import path
from app import views

urlpatterns = [
    path('create/user/', views.create_user),
    path('get/users/', views.get_user),
    path('get/user/<int:user_id>/', views.get_user_by_id),
    path('update/user/<int:user_id>/', views.update_user),
    path('delete/user/<int:user_id>/', views.delete_user),
]