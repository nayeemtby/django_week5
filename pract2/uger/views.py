from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

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
