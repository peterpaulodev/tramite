from cgitb import handler
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def handler404(request, exception):
    return render(request, 'base/not_found.html')
