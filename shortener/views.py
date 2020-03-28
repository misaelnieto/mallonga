from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from django import forms

from .models import UrlModel


class UrlForm(forms.Form):
    url = forms.CharField(label='Shorten the URL', max_length=2000)



# Create your views here.
def serve_short_url(request, code):
    urlobj = get_object_or_404(UrlModel, code=code)
    urlobj.hits += 1
    urlobj.save()
    return redirect(urlobj.url, permanent=True)


def home(request, template_name="home.html"):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            urlobj = UrlModel(url=form['url'])
            urlobj.save()
    else:
        form = UrlForm()

    return render(request, 'name.html', RequestContext(request, {'form': form}))
