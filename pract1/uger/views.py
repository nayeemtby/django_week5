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


def home(req):
    return render(req, 'index.html')


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
                return redirect('profile')
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


def profile(req):
    return render(req, 'profile.html')


@login_required
def changePassword(req):
    ctx: dict[str, object] = {
        'title': 'Change password',
        'btnTxt': 'Submit'
    }

    if req.method == 'GET':
        ctx['form'] = PasswordChangeForm(req.user)
    elif req.method == 'POST':
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            messages.success(req, 'Password successfully changed')
            return redirect('profile')
        else:
            ctx['form'] = form
    else:
        return badReq

    return render(req, 'form.html', ctx)


@login_required
def resetPass(req):
    ctx: dict[str, object] = {
        'title': 'Set password',
        'btnTxt': 'Submit'
    }

    if req.method == 'GET':
        ctx['form'] = SetPasswordForm(req.user)
    elif req.method == 'POST':
        form = SetPasswordForm(req.user, req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            messages.success(req, 'Password successfully reset')
            return redirect('profile')
        else:
            ctx['form'] = form
    else:
        return badReq

    return render(req, 'form.html', ctx)
