from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Instructor
from .forms import InstructorForm
from main.functions import clean_string

# Create your views here.
@login_required
def index(request):
    instructors = Instructor.objects.all()

    data = {
            'has_datatable': True,
            'instructors': instructors
            }

    return render(request, 'instructor/index.html', data)

@login_required
def create(request):
    if request.method == 'POST':
        instructor_form = InstructorForm(request.POST)

        if instructor_form.is_valid():
            instructor = instructor_form.save(commit=False)
            instructor.cpf = clean_string(instructor.cpf)
            instructor.rg = clean_string(instructor.rg)
            instructor.primary_phone = clean_string(instructor.primary_phone)
            instructor.secondary_phone = clean_string(instructor.secondary_phone)

            instructor.save()
            return redirect('/instructor')
    else:
        instructor_form = InstructorForm()
        return render(request, 'instructor/create.html', {'instructor_form': instructor_form})

@login_required
def edit(request, id):
    instructor = get_object_or_404(Instructor, pk=id)
    instructor_form = InstructorForm(instance=instructor)

    if request.method == 'POST':
        instructor_form = InstructorForm(request.POST, instance=instructor)

        if instructor_form.is_valid():
            instructor_form.save()
            return redirect('/instructor')

    else:
        return render(request, 'instructor/edit.html', {'instructor': instructor, 'instructor_form': instructor_form})
