from django.test import TestCase
from shortener.models import random_hash, UrlModel



class HashTests(TestCase):
    def test_hash(self):
        # The hash is pretty simple. We will use a proper hashing function later
        h = random_hash()
        self.assertIsInstance(h, str)
        self.assertEqual(len(h), 5)

    def test_url_model(self):
        url = UrlModel(url="http://example.com/abcd/efg.htmla=4324225434324&b=ddasda")
        self.assertEqual(url.code, '', 'The code doesnot exists yet')
        url.save()
        self.assertNotEqual(url.code, 'Upon saving, the code has been generated')