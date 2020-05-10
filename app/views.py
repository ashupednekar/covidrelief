from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from covidrelief.settings import SERVER_HOST

from localusers.models import LocalUser
from app.models import Centers
from django.http import HttpResponse


"""RENDER VIEWS"""


@login_required
def index(request):
    if request.user.role != 'operator':
        data = dict(LocalUser.objects.filter(username=request.user).values()[0])
        return render(request, 'frontend/home.html', {
            'data': data,
            'host': SERVER_HOST
        })
    else:
        return render(request, 'frontend/entries.html', {
            'host': SERVER_HOST
        })

@login_required
def centers(request):
    if request.user.role == 'admin':
        return render(request, 'frontend/centers.html', {
            'host': SERVER_HOST
        })
    else:
        return HttpResponse('Invalid role')

@login_required
def entries(request):
    return render(request, 'frontend/entries.html', {
        'host': SERVER_HOST,
        'table': [['aaa', 'aaa', 'aaa','aaa','aaa','aaa','aaa','aaa','aaa'], ['aaa', 'aaa', 'aaa','aaa','aaa','bbb','bbb','bbb','bbb']]
    })

@login_required
def closed(request):
    if request.user.role in ['admin', 'manager']:
        return render(request, 'frontend/closed.html', {
            'host': SERVER_HOST
        })
    else:
        return HttpResponse('Invalid Role')


@login_required
def assign(request):
    if request.user.role == 'admin':
        return render(request, 'frontend/assign.html', {
            'host': SERVER_HOST
        })
    else:
        return HttpResponse('Invalid Role')
