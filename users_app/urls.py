from django.contrib import admin
from django.urls import path
from users_app.views import getAllAdmins, createAdmin, getAdmin, deleteAdmin, updateAdmin

urlpatterns = [
    path('getAdmins/', getAllAdmins, name="Get All Admins"),
    path('createAdmin/', createAdmin, name="Create New Admin"),
    path('getAdmin/<int:pk>/', getAdmin, name="Get Single Admin"),
    path('deleteAdmin/<int:pk>/', deleteAdmin, name="Delete Admin"),
    path('updateAdmin/<int:pk>/', updateAdmin, name="Update Admin"),
]