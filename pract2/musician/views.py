from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from musician.forms import MusicianForm
from musician.models import Musician

# Create your views here.

notAllowed = HttpResponseNotAllowed(['GET', 'POST'])


class AddMusicianView(SuccessMessageMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'btnTxt': 'Add Musician',
        'title': 'Add Musician'
    }
    success_message = 'Musician added'


class EditMusicianView(SuccessMessageMixin, UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    extra_context = {
        'btnTxt': 'Update Musician',
        'title': 'Edit Musician'
    }
    success_message = 'Musician updated successfully'


class DeleteMusicianView(SuccessMessageMixin, DeleteView):
    model = Musician
    template_name = 'musician_form.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    extra_context = {
        'btnTxt': 'Delete Musician',
        'title': 'Delete Musician'
    }
    success_message = 'Musician and related albums deleted successfully'
