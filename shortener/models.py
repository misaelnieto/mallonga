import string
import random
from django.urls import reverse
from django.db import models

def random_hash():
    """
    TODO: This is just a placeholder function. We will remove it later
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=5))


class UrlModel(models.Model):
    code = models.TextField(auto_created=True, unique=True)
    url = models.TextField()
    title = models.TextField()
    cover = models.TextField()
    hits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.code = random_hash()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("short_url", kwargs={"code": self.code})
