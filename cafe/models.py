from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    contents=models.TextField(help_text='Markdown 문법을 써주세요.')
    tags=models.CharField(max_length=100, blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    writer=models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title

class Reply(models.Model):
    content=models.TextField(help_text='Markdown 문법을 써주세요.')
    created_at=models.DateTimeField(default=timezone.now)
    writer=models.ForeignKey(settings.AUTH_USER_MODEL)
    at=models.ForeignKey(Post)


    def __str__(self):
        return self.content

