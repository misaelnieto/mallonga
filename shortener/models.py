import string
import random
from urllib.request import urlopen

from django.urls import reverse
from django.db import models
from django.conf import settings

from bs4 import BeautifulSoup


def random_hash():
    """
    TODO: This is just a placeholder function. We will remove it later
    """
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choices(alphabet, k=8))


class UrlModel(models.Model):
    code = models.TextField(auto_created=True, unique=True)
    url = models.TextField()
    title = models.TextField()
    cover = models.TextField()
    hits = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = random_hash()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        if hasattr(settings, 'APP_DOMAIN'):
            proto = getattr(settings, 'APP_HTTPS', False) and 'https' or 'http'
            domain = settings.APP_DOMAIN
            return f'{proto}://{domain}/{self.code}'
        return reverse('short_url', args=[self.code,])

    def process_url(self):
        with urlopen(self.url) as response:
            soup = BeautifulSoup(response, 'html.parser')
            if soup.title:
                self.title = soup.title.text
            else:
                self.title = self.url
