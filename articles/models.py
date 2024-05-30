from django.db import models
from django.utils import timezone
from math import floor
from datetime import timedelta
from django.utils.timesince import timesince


class Article(models.Model):
    title = models.CharField(max_length=100, default='Default title')
    description = models.TextField(default='Default description')
    content = models.TextField(default='Default content')
    author = models.CharField(max_length=100, default='Terry Davis')
    published_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def serializer_all(self):
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "description": self.description,
            'created_at': self.whenAdded(),
        }
    
    def serializer_single(self):
        return {
            "id": self.id,
            "author": self.author,
            "title": self.title,
            "description": self.description,
            'created_at': self.whenAdded(),
            'content': self.content
        }
    
    def whenAdded(self):
        now = timezone.now()
        diff = now - self.published_date

        if diff <= timedelta(minutes=29):
            return 'Just now'
        elif diff <= timedelta(minutes=59):
            return '30 minutes ago'
        elif diff <= timedelta(hours=23):
            return str(diff.seconds//3600) + ' hours ago'
        elif diff <= timedelta(days=6):
            return str(diff.days) + ' days ago'
        elif diff <= timedelta(weeks=4):
            return str(diff.days//7) + ' weeks ago'
        else:
            return str(diff.days//30) + ' months ago'
        #return f'{timesince(self.published_date)} ago'
            