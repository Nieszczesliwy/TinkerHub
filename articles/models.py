from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, default='Default title')
    description = models.CharField(max_length=400, default='Default description')
    content = models.TextField(default='Default content')
    author = models.CharField(max_length=100, default='Terry Davis')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title