from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Classes
from instructor.models import Instructor
from .forms import ClassesForm

# Create your views here.
def index(request):
    classes = Classes.objects.all()

    data = {
            'has_datatable': True,
            'classes': classes
            }

    return render(request, 'class/index.html', data)


def create(request):
    class_form = ClassesForm()

    instructors = Instructor.objects.all()
    return render(request, 'class/create.html', {'instructors': instructors, 'class_form': class_form})


def edit(request, id):
    instructors = Instructor.objects.all()
    _class = get_object_or_404(Classes, pk=id)

    return render(request, 'class/edit.html', {'class': _class, 'instructors': instructors})

def newClass(request):
    return render(request, 'class/create.html')
