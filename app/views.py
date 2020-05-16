from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from covidrelief.settings import SERVER_HOST

from localusers.models import LocalUser
from app.models import *
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
        entries = Entries.objects.filter(closed='N', actor=request.user.username)
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
        return render(request, 'frontend/entries.html', {
            'host': SERVER_HOST,
            'table': res
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
def stocks(request):
    if request.user.role == 'admin':
        valueslist = list(Shipments.objects.all().values())
    elif request.user.role == 'manager':
        valueslist = list(Shipments.objects.filter(center=request.user.center).values())
    else:
        return HttpResponse('Invalid role')
    entrytable = list()
    for x in valueslist:
        x['timestamp'] = x['timestamp'].strftime("%m/%d/%Y")
        entrytable.append(x)
    print(entrytable)
    if list(Stocks.objects.all().values()):
        total = Stocks.objects.all().values()[0]['count']
    else:
        total = 0
    try:
        center_specific = Centers.objects.filter(center_name=request.user.center).values()[0]['stock_count']
    except IndexError: #center unassigned
        center_specific = 0
    if request.user.role == 'admin' or request.user.role == 'manager':
        return render(request, 'frontend/stocks.html', {
            'host': SERVER_HOST,
            'total': total,
            'center_specific': center_specific,
            'center_stocks': list(Centers.objects.all().values()),
            'table': entrytable
        })
    else:
        return HttpResponse('Invalid role')


@login_required
def entries(request):
    if request.user.role == 'admin':
        entries = Entries.objects.filter(closed='N')
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
    elif request.user.role == 'manager':
        entries = Entries.objects.filter(closed='N', center=request.user.center)
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
    elif request.user.role == 'operator':
        entries = Entries.objects.filter(closed='N', actor=request.user.username)
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
    else:
        raise RuntimeError
    # valueslist = list(Entries.objects.filter(closed='N').values())
    # entrytable = list()
    # for x in valueslist:
    #     x['date_received'] = x['date_received'].strftime("%m/%d/%Y")
    #     entrytable.append(x)
    print('table: ', res)
    return render(request, 'frontend/entries.html', {
        'host': SERVER_HOST,
        'table': res
    })


@login_required
def closed(request):
    if request.user.role == 'admin':
        entries = Entries.objects.filter(closed='Y')
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
    elif request.user.role == 'manager':
        entries = Entries.objects.filter(closed='Y', center=request.user.center)
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
    elif request.user.role == 'operator':
        entries = Entries.objects.filter(closed='Y', actor=request.user.username)
        res = list(entries.values())
        for r in res:
            r['date_received'] = r['date_received'].strftime("%m/%d/%Y")
    else:
        raise RuntimeError
    # valueslist = list(Entries.objects.filter(closed='N').values())
    # entrytable = list()
    # for x in valueslist:
    #     x['date_received'] = x['date_received'].strftime("%m/%d/%Y")
    #     entrytable.append(x)
    print('table: ', res)
    return render(request, 'frontend/entries.html', {
        'host': SERVER_HOST,
        'table': res
    })


@login_required
def assign(request):
    if request.user.role == 'admin':
        return render(request, 'frontend/assign.html', {
            'host': SERVER_HOST
        })
    else:
        return HttpResponse('Invalid Role')