from django.db import models
from system_users_app.models import User

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title