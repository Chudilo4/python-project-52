from django.shortcuts import render
from django.utils.translation import gettext


def index(request):
    out = gettext('Hello')
    return render(request, 'home.html', {'output': out})

