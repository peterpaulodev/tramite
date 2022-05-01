from cgitb import handler
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'main/index.html')

def handler404(request, exception):
    return render(request, 'base/not_found.html')
