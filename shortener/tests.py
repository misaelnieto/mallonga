from unittest import mock
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
    def test_url_fetch(self):
        link = UrlModel(
            url='https://example.com/abcd/efg.html',
            title='My Awesome Site',
        )

        response = self.client.get('https://chiqui.to/a4fFd56')
        self.assertEqual(response.status, '301')
        self.assertEqual(response.headers['Location'], link.url)
        self.assertEqual(link.hits, 0)


class Top100TestCase(TestCase):
    def test_top100_links(self):
        foobar()
        self.assertEqual(something, 1000)
