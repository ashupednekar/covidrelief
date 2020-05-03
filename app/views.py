from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from covidrelief.settings import SERVER_HOST

from localusers.models import LocalUser
from app.models import Centers


"""RENDER VIEWS"""


@login_required
def index(request):
    data = dict(LocalUser.objects.filter(username=request.user).values()[0])
    return render(request, 'frontend/home.html', {
        'data': data,
        'host': SERVER_HOST
    })


@login_required
def centers(request):
    return render(request, 'frontend/centers.html', {
        'host': SERVER_HOST
    })

@login_required
def entries(request):
    return render(request, 'frontend/entries.html', {
        'host': SERVER_HOST
    })


@login_required
def assign(request):
    return render(request, 'frontend/assign.html', {
        'host': SERVER_HOST
    })
