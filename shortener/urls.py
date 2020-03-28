from django.urls import path
from .views import serve_short_url, home

urlpatterns = [
    path('?P<code>[\w]+', serve_short_url, name='short_url'),
    path('', home, name='home'),
]
