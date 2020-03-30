from django.urls import path
from .views import serve_short_url, home, top100

urlpatterns = [
    path('top100', top100, name='top100'),
    path('<slug:code>', serve_short_url, name='short_url'),
    path('', home, name='home'),
]
