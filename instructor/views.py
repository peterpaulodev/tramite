import re
from urllib.request import Request
from colorama import Back
from django.forms import NullBooleanField
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

import instructor
from .models import Instructor, InstructorDocuments
from .forms import InstructorDocumentsForm, InstructorForm
from django.contrib import messages

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
            instructor_form.save()
            messages.success(request, 'Instrutor salvo com sucesso!')

            return redirect('/instructor')
        else:
            messages.error(request, 'Erro ao validar o cadastro de instrutor!')
            return redirect('/instructor/create')

    else:
        instructor_form = InstructorForm()
        return render(request, 'instructor/create.html', {'instructor_form': instructor_form})


@login_required
def edit(request, id):
    instructor = get_object_or_404(Instructor, pk=id)
    instructor_form = InstructorForm(instance=instructor)

    try:
        documents = InstructorDocuments.objects.get(
            instructor=id)

    except InstructorDocuments.DoesNotExist:
        documents = False

    data = {
        'documents': documents,
        'instructor': instructor,
        'instructor_form': instructor_form
    }

    if request.method == 'POST':
        instructor_form = InstructorForm(request.POST, instance=instructor)

        if instructor_form.is_valid():
            instructor_form.save()

            data['instructor_form'] = instructor_form
            messages.success(request, 'Instrutor editado com sucesso!')

            return render(request, 'instructor/edit.html', data)

        else:
            messages.error(request, 'Erro ao validar o cadastro de instrutor!')
            return render(request, 'instructor/edit.html', data)

    else:
        return render(request, 'instructor/edit.html', data)


@login_required
def upload_instructor_document(request):
    if request.method == "POST":
        instructor_id = request.POST["instructor"]
        file_list = request.FILES

        print(Back.BLUE, "==>> instructor_documents: ", file_list)

        try:
            documents = InstructorDocuments.objects.get(
                instructor=instructor_id)

            instructor_documents = InstructorDocumentsForm(
                request.POST, request.FILES, instance=documents)

        except InstructorDocuments.DoesNotExist:
            instructor_documents = InstructorDocumentsForm(
                request.POST, request.FILES)

        if instructor_documents.is_valid():
            instructor_documents.save()

            messages.success(request, 'Documento salvo com sucesso!')
            return redirect('/instructor/edit/' + str(instructor_id))
        else:
            messages.error(request, 'Erro ao salvar os documentos!')
            print(Back.RED, "==>> class_form: ",
                  instructor_documents.errors.as_json())

            return redirect('/instructor/edit/' + str(instructor_id))
    else:
        return redirect('/instructor/edit/' + str(instructor_id))


@login_required
def ready_documents(request, id, ready):
    instructor = get_object_or_404(Instructor, pk=id)
    instructor.ready_documents = bool(ready)
    instructor.save()

    messages.success(request, 'Status da documentação atualizado!')
    return redirect('/instructor/edit/' + str(id))


