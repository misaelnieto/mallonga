import urllib
from django.core.management.base import BaseCommand, CommandError
from shortener.models import UrlModel


class Command(BaseCommand):
    help = 'Retrieve the title of all the urls which have an empty title'

    def handle(self, *args, **options):
        for link in UrlModel.objects.filter(title = ''):
            try:
                link.process_url()
            except urllib.error.URLError:
                link.title = 'N/A'
            link.save()

        # self.stdout.write(self.style.SUCCESS('All links were processed.'))