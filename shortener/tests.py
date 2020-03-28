from unittest import mock
from django.test import TestCase
from django.urls import reverse
from shortener.models import random_hash, UrlModel



class HashTests(TestCase):
    def test_hash(self):
        # The hash is pretty simple. We will use a proper hashing function later
        h = random_hash()
        self.assertIsInstance(h, str)
        self.assertEqual(len(h), 8)

    def test_url_model(self):
        url = UrlModel(url="http://example.com/abcd/efg.htmla=4324225434324&b=ddasda")
        self.assertEqual(url.code, '', 'The code doesnot exists yet')
        url.save()
        self.assertNotEqual(url.code, 'Upon saving, the code has been generated')


mock_page = b'''
<html>
<head><title>My awesome page!</title></head>
<body>Hello world!</body>
</html>
'''


class UrlProcessTestCase(TestCase):
    @mock.patch('shortener.models.urlopen')
    def test_url_fetch_task(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value = mock_page

        # A user creates an URL
        link = UrlModel(url='https://example.com/abcd/efg.html')

        # The task queue process the url in the background
        link.process_url()

        # The task fetched the title
        self.assertEqual(link.title, 'My awesome page!')


class UrlHitTestCase(TestCase):
    def test_url_redirect(self):
        link = UrlModel(
            url='https://example.com/abcd/efg.html',
            title='My Awesome Site',
        )
        link.save()
        self.assertEqual(link.hits, 0)

        response = self.client.get(link.get_absolute_url())
        self.assertEqual(response.status_code, 301)
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.get('Location'), link.url)
        link.refresh_from_db()
        self.assertEqual(link.hits, 1)


class Top100TestCase(TestCase):
    def test_top100_links(self):
        foobar()
        self.assertEqual(something, 1000)
