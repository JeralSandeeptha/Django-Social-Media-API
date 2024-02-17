from django.db import models

class Admin(models.Model):
    adminId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username
    