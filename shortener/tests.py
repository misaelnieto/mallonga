from unittest import mock

from bs4 import BeautifulSoup

from django.test import TestCase
from django.urls import reverse
from shortener.models import random_hash, UrlModel



class HashTests(TestCase):
    def test_hash(self):
        # The hash is pretty simple. We can use a proper hashing function later
        h = random_hash()
        self.assertIsInstance(h, str)
        self.assertEqual(len(h), 8)

    def test_url_model(self):
        url = UrlModel(url="http://example.com/abcd/efg.htmla=4324225434324&b=ddasda")
        self.assertEqual(url.code, '', 'The code doesnot exists yet')
        url.save()
        self.assertNotEqual(url.code, '', 'Upon saving, the code has been generated')


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

        # Django settings does not have the APP_DOMAIN setting yet
        response = self.client.get(link.get_absolute_url())
        self.assertEqual(response.status_code, 301)
        self.assertTrue(response.has_header('Location'))
        self.assertEqual(response.get('Location'), link.url)
        link.refresh_from_db()
        self.assertEqual(link.hits, 1)

    def test_absolute_url(self):
        link = UrlModel(
            url='https://example.com/abcd/efg.html',
            title='My Awesome Site',
        )
        link.save()

        url = link.get_absolute_url()
        self.assertEqual(link.get_absolute_url(), f'/{link.code}')

        with self.settings(APP_DOMAIN='e.ta'):
            url = link.get_absolute_url()
            self.assertEqual(link.get_absolute_url(), f'http://e.ta/{link.code}')

        with self.settings(APP_DOMAIN='e.ta', APP_HTTPS=False):
            url = link.get_absolute_url()
            self.assertEqual(link.get_absolute_url(), f'http://e.ta/{link.code}')

        with self.settings(APP_DOMAIN='e.ta', APP_HTTPS=True):
            url = link.get_absolute_url()
            self.assertEqual(link.get_absolute_url(), f'https://e.ta/{link.code}')


    def test_home(self):
        # Initially, we don't hava any url
        self.assertEquals(UrlModel.objects.count(), 0)

        # Now let's visit home and submit an url
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        soup = BeautifulSoup(resp.content, 'html.parser')

        # We should have an empty form on that page
        self.assertEqual(soup.form.attrs, {'method': 'POST', 'action': '/'})
        self.assertTrue(soup.form.input.getText() == '')

        # Now let's post a url
        resp = self.client.post(
            reverse('home'),
            {'url': 'http://www.example.com/biz/bas/foo/bar.html'}
        )
        self.assertEquals(UrlModel.objects.count(), 1)


class Top100TestCase(TestCase):
    fixtures = ['shortener/fixtures/links.json']
    def test_top100_links(self):
        with self.settings(APP_DOMAIN='e.ta', APP_HTTPS=False):
            resp = self.client.get(reverse('top100'))
            soup = BeautifulSoup(resp.content, 'html.parser')
            table = soup.find('table', class_="top100")
            rows = len(table.tbody.findAll('tr'))
            self.assertEqual(rows, 100)
