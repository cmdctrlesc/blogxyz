from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    subtitle = models.TextField(default=" ")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
