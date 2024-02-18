from django.urls import path
from .views import get_comment, get_comments, get_comments_by_postId, delete_comment, create_comment, update_comment

urlpatterns = [
    path('getComments/', get_comments, name="Get All Comments"),
    path('createComment/', create_comment, name="Create New Comment"),
    path('getComment/<int:pk>/', get_comment, name="Get Single Comment"),
    path('deleteComment/<int:pk>/', delete_comment, name="Delete Comment"),
    path('updateComment/<int:pk>/', update_comment, name="Update Comment"),
    path('getCommentsByPostId/<int:postId>/', get_comments_by_postId, name="Get All Comment By User Id"),
]