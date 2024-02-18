from django.db import models
from posts_app.models import Post
from system_users_app.models import User

class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment