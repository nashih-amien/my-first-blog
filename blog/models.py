from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone



class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tag = models.ManyToManyField(Tag)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.post}: {self.content[:50]}"

class Profile(models.Model):
    user = models.OneToOneField(Post, on_delete=models.CASCADE)
    bio = models.TextField()
