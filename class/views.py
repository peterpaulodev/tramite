from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Classes
from instructor.models import Instructor
from .forms import ClassesForm
from django.contrib import messages
from colorama import Fore, Back, Style
from datetime import datetime
from main.functions import clean_string

# Create your views here.
@login_required
def index(request):
    classes = Classes.objects.all()

    data = {
            'has_datatable': True,
            'classes': classes
            }

    return render(request, 'class/index.html', data)

@login_required
def create(request):
    if request.method == 'POST':
        updated_request = request.POST.copy()

        initial_date = datetime.strptime(updated_request['initial_date'], "%d/%m/%Y")
        finish_date = datetime.strptime(updated_request['finish_date'], "%d/%m/%Y")
        zipcode = clean_string(updated_request['zipcode'])

        changed_data = {
            'initial_date': initial_date,
            'finish_date': finish_date,
            'zipcode': zipcode
        }

        updated_request.update(changed_data)
        class_form = ClassesForm(updated_request)

        if class_form.is_valid():
            class_form.save()
            messages.success(request, 'Curso salvo com sucesso!')

            return redirect('/class')
        else:
            messages.error(request, 'Erro ao validar o cadastro do curso!')
            print(Back.RED, "==>> class_form: ", class_form.errors.as_json())

            return redirect('/class/create')

    else:
        class_form = ClassesForm()
        instructors = Instructor.objects.all()
        return render(request, 'class/create.html', {'instructors': instructors, 'class_form': class_form})

@login_required
def edit(request, id):
    instructors = Instructor.objects.all()

    _class = get_object_or_404(Classes, pk=id)
    class_form = ClassesForm(instance=_class)

    if request.method == 'POST':
        updated_request = request.POST.copy()

        initial_date = datetime.strptime(updated_request['initial_date'], "%d/%m/%Y")
        finish_date = datetime.strptime(updated_request['finish_date'], "%d/%m/%Y")
        zipcode = clean_string(updated_request['zipcode'])

        changed_data = {
            'initial_date': initial_date,
            'finish_date': finish_date,
            'zipcode': zipcode
        }

        updated_request.update(changed_data)
        class_form = ClassesForm(updated_request, instance=_class)

        if class_form.is_valid():
            class_form.save()

            messages.success(request, 'Curso editado com sucesso!')

        else:
            messages.error(request, 'Erro ao validar o cadastro do curso!')
            print(Back.RED, "==>> class_form: ", class_form.errors.as_json())

        return render(request, 'class/edit.html', {'class': _class, 'class_form': class_form, 'instructors': instructors})

    else:
        return render(request, 'class/edit.html', {'class': _class, 'class_form': class_form, 'instructors': instructors})

def newClass(request):
    return render(request, 'class/create.html')
