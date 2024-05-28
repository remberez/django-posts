from django.db import models
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_changed = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post', args=[self.id])
