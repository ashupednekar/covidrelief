from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from localusers.models import LocalUser

@login_required
def index(request):
    data = dict(LocalUser.objects.filter(username=request.user).values()[0])
    return render(request, 'frontend/index.html', data)