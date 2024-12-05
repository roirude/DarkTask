from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    statut = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)