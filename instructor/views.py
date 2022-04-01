from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Instructor

# Create your views here.
def index(request):
    instructors = Instructor.objects.all()

    data = {
            'has_datatable': True,
            'instructors': instructors
            }

    return render(request, 'instructor/index.html', data)


def create(request):
    return render(request, 'instructor/create.html')


def edit(request, id):
    instructor = get_object_or_404(Instructor, pk=id)

    return render(request, 'instructor/edit.html', {'instructor': instructor})
