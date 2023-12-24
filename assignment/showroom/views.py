from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from showroom.forms import CommentForm
from django.contrib import messages
from django.views.generic import ListView

from showroom.models import Brand, Car, Comment, Transaction

# Create your views here.


# def home(req: HttpRequest):
#     ctx: dict[str, object] = {}
#     ctx['cars'] = Car.objects.all()
#     return render(req, 'index.html', ctx)


class HomeView(ListView):
    model = Car
    context_object_name = 'cars'
    template_name = 'index.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        extra_context = {
            'brands': Brand.objects.all(),
        }

        brandId = request.GET.get('brand')
        if brandId is not None:
            brand = Brand.objects.filter(pk=brandId).get()
            self.queryset = Car.objects.filter(brand=brand)
        else:
            self.queryset = Car.objects.all()

        self.extra_context = extra_context
        return super().get(request, *args, **kwargs)


def carDetails(req: HttpRequest, id):
    ctx: dict[str, object] = {}
    car = Car.objects.filter(pk=id).get()
    ctx['car'] = car
    form = CommentForm()
    if req.method == 'POST':
        form = CommentForm(req.POST)
        form.instance.car = car
        if form.is_valid():
            form.save()
            form = CommentForm()
    ctx['form'] = form
    ctx['comments'] = Comment.objects.filter(car=car).values()
    return render(req, 'details.html', ctx)


@login_required
def buyCar(req: HttpRequest, id):
    car = Car.objects.filter(pk=id).get()
    if car.stock == 0:
        return redirect('carDetails', id)
    car.stock = car.stock-1
    car.save()
    Transaction(car=car, user=req.user).save()
    messages.success(req, 'You bought a '+car.brand.name+' '+car.name)
    return redirect('profile')
