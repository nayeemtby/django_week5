from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

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


@login_required
def deleteMusician(req, id):
    Musician.objects.get(pk=id).delete()
    return redirect('home')
