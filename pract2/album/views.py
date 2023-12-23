from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from album.forms import AlbumForm
from album.models import Album

# Create your views here.

notAllowed = HttpResponseNotAllowed(['GET', 'POST'])


class AddAlbumView(SuccessMessageMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'btnTxt': 'Add',
        'title': 'Add Album'
    }
    success_message = 'Album added'


class EditAlbumView(SuccessMessageMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    extra_context = {
        'btnTxt': 'Update Album',
        'title': 'Edit Album'
    }
    success_message = 'Album updated successfully'
