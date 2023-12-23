from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from uger.forms import ProfileUpdateForm, RegistrationForm

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


class CLoginView(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    extra_context = {
        'title': 'Login',
        'btnTxt': 'login'
    }

    success_message = 'Logged in successfully'

    def get_success_url(self) -> str:
        return reverse_lazy('home')


def logout(req: HttpRequest):
    if req.user.is_authenticated:
        req.session.clear()
        messages.success(req, 'Logged Out Successfully')
    return redirect('home')


def profileView(req: HttpRequest):
    req.user
    return render(req, 'profile.html')


def updateProfileView(req: HttpRequest):
    ctx: dict[str, object] = {
        'btnTxt': 'Update',
        'title': 'Update profile'
    }
    if req.method == 'GET':
        ctx['form'] = ProfileUpdateForm(instance=req.user)
        return render(req, 'form.html', ctx)
    elif req.method == 'POST':
        form = ProfileUpdateForm(req.POST, instance=req.user)
        if form.is_valid():
            form.save(commit=True)
            messages.success(req, 'Profile updated successfully')
            return redirect('profile')
        else:
            ctx['form'] = form
            return render(req, 'form.html', ctx)
    return badReq
