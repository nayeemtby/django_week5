from django.shortcuts import render

from album.models import Album

# Create your views here.


def home(req):
    albums = Album.objects.all()
    ctx = {'albums': albums}
    return render(req, 'index.html', ctx)
