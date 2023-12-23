from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render

from album.forms import AlbumForm
from album.models import Album

# Create your views here.

notAllowed = HttpResponseNotAllowed(['GET', 'POST'])

def addAlbum(req: HttpRequest):
    ctx: dict[str, object] = {'btnTxt': 'Add Album',
                              'title': 'Add Album'}
    if req.method == 'GET':
        ctx['form'] = AlbumForm()
        return render(req, 'album_form.html', ctx)
    elif req.method == 'POST':
        form = AlbumForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            ctx['form'] = form
            return render(req, 'album_form.html', ctx)
    return notAllowed


def editAlbum(req, id):
    ctx: dict[str, object] = {
        'btnTxt': 'Update Album', 'title': 'Edit Album'}
    if req.method == 'GET':
        album = Album.objects.get(pk=id)
        ctx['form'] = AlbumForm(instance=album)
        return render(req, 'album_form.html', ctx)
    elif req.method == 'POST':
        form = AlbumForm(req.POST, instance=Album.objects.get(pk=id))
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            ctx['form'] = form
            return render(req, 'album_form.html', ctx)
    return notAllowed
