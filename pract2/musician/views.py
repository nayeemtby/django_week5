from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from musician.forms import MusicianForm
from musician.models import Musician

# Create your views here.

notAllowed = HttpResponseNotAllowed(['GET', 'POST'])


@login_required
def addMusician(req: HttpRequest):
    ctx: dict[str, object] = {'btnTxt': 'Add Musician',
                              'title': 'Add Musician'}
    if req.method == 'GET':
        ctx['form'] = MusicianForm()
        return render(req, 'musician_form.html', ctx)
    elif req.method == 'POST':
        form = MusicianForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            print('Form not valid or no function')
            ctx['form'] = form
            return render(req, 'musician_form.html', ctx)
    return notAllowed


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


@login_required
def editMusician(req: HttpRequest, id):
    ctx: dict[str, object] = {
        'btnTxt': 'Update Musician', 'title': 'Edit Musician'}
    if req.method == 'GET':
        musician = Musician.objects.get(pk=id)
        ctx['form'] = MusicianForm(instance=musician)
        return render(req, 'musician_form.html', ctx)
    elif req.method == 'POST':
        form = MusicianForm(req.POST, instance=Musician.objects.get(pk=id))
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
        else:
            ctx['form'] = form
            return render(req, 'musician_form.html', ctx)
    return notAllowed


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


@login_required
def deleteMusician(req, id):
    Musician.objects.get(pk=id).delete()
    return redirect('home')
