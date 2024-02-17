from django.db import models

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title