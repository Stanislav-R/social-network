from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}'s post"

    class Meta:
        ordering = ['-created']
