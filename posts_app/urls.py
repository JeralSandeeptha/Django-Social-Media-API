from django.contrib import admin
from django.urls import path
from .views import get_post, get_posts, create_post, update_post, delete_post, get_posts_by_userId

urlpatterns = [
    path('getPosts/', get_posts, name="Get All Posts"),
    path('createPost/', create_post, name="Create New Post"),
    path('getPost/<int:pk>/', get_post, name="Get Single Post"),
    path('deletePost/<int:pk>/', delete_post, name="Delete Post"),
    path('updatePost/<int:pk>/', update_post, name="Update Post"),
    path('getPostsByUserId/<int:userId>/', get_posts_by_userId, name="Get All Posts By User Id"),
]