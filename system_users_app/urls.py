from django.urls import path
from .views import get_users, create_user, get_user, update_user, delete_user

urlpatterns = [
    path('getUsers/', get_users, name="Get All Users"),
    path('createUser/', create_user, name="Create New User"),
    path('getUser/<int:pk>/', get_user, name="Get Single User"),
    path('deleteUser/<int:pk>/', delete_user, name="Delete User"),
    path('updateUser/<int:pk>/', update_user, name="Update User"),
]