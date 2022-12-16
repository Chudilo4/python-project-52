from django.shortcuts import render
from django.utils.translation import gettext
from django.http import HttpResponse

def index(request):
    output = gettext("Navbar example")
    #return render(request, 'home.html', {'output': output})
    return HttpResponse(output)
