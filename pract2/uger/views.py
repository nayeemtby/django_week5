from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from uger.forms import RegistrationForm

# Create your views here.

badReq = HttpResponseNotAllowed('GET', 'POST')


def register(req: HttpRequest):
    ctx: dict[str, object] = {
        'title': 'Sign up',
        'btnTxt': 'Submit'
    }

    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'GET':
        ctx['form'] = RegistrationForm()
    elif req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')
        else:
            ctx['form'] = form
    else:
        return badReq

    return render(req, 'form.html', ctx)


def loginView(req):
    ctx: dict[str, object] = {
        'title': 'Login',
        'btnTxt': 'login'
    }

    if req.user.is_authenticated:
        return redirect('home')

    if req.method == 'GET':
        ctx['form'] = AuthenticationForm()
    elif req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(req, user)
                messages.success(req, 'Logged In Successfully')
                return redirect('home')
            else:
                print('Setting message')
                ctx['form'] = form
        else:
            ctx['form'] = form
    else:
        return badReq

    return render(req, 'form.html', ctx)


def logout(req: HttpRequest):
    if req.user.is_authenticated:
        req.session.clear()
        messages.success(req, 'Logged Out Successfully')
    return redirect('home')
