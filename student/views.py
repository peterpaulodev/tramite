import os
from this import d
from colorama import Back
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from main.functions import clean_string, logo_tramite_base64
from student.models import DocumentObservation, DocumentStatus, Student, StudentDocuments
from django.contrib import messages
from student.forms import DocumentObservationForm, DocumentStatusForm, StudentDocumentsForm, StudentForm
from datetime import datetime
import pdfkit
from django.template.loader import render_to_string
from django.core.mail import send_mail

CONFIG = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

# Create your views here.


@login_required
def index(request):
    students = Student.objects.all()

    data = {
        'has_datatable': True,
        'students': students
    }

    return render(request, 'student/index.html', data)


@login_required
def edit(request, id):
    student = get_object_or_404(Student, pk=id)
    student_form = StudentForm(instance=student)

    documents = False
    status = False
    observations = False

    try:
        documents = StudentDocuments.objects.get(student=id)
    except StudentDocuments.DoesNotExist:
        documents = False

    try:
        status = DocumentStatus.objects.get(student=id)
    except StudentDocuments.DoesNotExist:
        status = False

    try:
        observations = DocumentObservation.objects.get(student=id)
        observation_form = DocumentObservationForm(instance=observations)
    except StudentDocuments.DoesNotExist:
        observations = False

    print(Back.RED, "==>> observation_form: ", observations)

    data = {
        'student': student,
        'status': status,
        'observation_form': observation_form,
        'documents': documents,
        'student_form': student_form
    }

    if request.method == 'POST':
        student_form = StudentDocuments(request.POST, instance=student)

        if student_form.is_valid():
            student_form.save()

            data['student_form'] = student_form
            messages.success(request, 'Aluno editado com sucesso!')

            return render(request, 'student/edit.html', data)

        else:
            messages.error(request, 'Erro ao validar o cadastro do aluno!')
            return render(request, 'student/edit.html', data)

    else:
        return render(request, 'student/edit.html', data)


def registration(request):
    if request.method == 'POST':
        updated_request = request.POST.copy()

        birth_date = datetime.strptime(
            updated_request['birth_date'], "%d/%m/%Y")
        zipcode = clean_string(updated_request['zipcode'])

        changed_data = {
            'birth_date': birth_date,
            'zipcode': zipcode
        }

        updated_request.update(changed_data)
        student_form = StudentForm(updated_request)

        if student_form.is_valid():
            try:
                Student.objects.get(cpf=student_form.data['cpf'])

                messages.error(request, 'Já existe um cadastro com esse CPF!')
                return redirect('/student/registration')
            except Student.DoesNotExist:
                student_form.save()
                student_id = str(student_form.instance.id)
                os.mkdir("media/student/" + student_id + "/")
                return redirect('/student/documentation/' + student_id)

        else:
            print(Back.RED, "==>> student_form: ",
                  student_form.errors.as_json())
            return redirect('/student/registration')

    else:
        student_form = StudentForm()
        return render(request, 'student/registration.html', {'student_form': student_form})


def pre_register_validation(request):
    student_form = StudentForm()

    if request.method == 'POST':
        cpf = request.POST['student-cpf']
        password = request.POST['student-password']

        try:
            student = Student.objects.get(cpf=cpf, password=password)
            print(Back.BLUE, "==>> student: ", student)

            return redirect('/student/documentation/' + str(student.id))
        except Student.DoesNotExist:
            messages.error(
                request, 'Não foi encontrado nenhum aluno com esses dados!')
            return redirect('/accounts/login')
    else:
        return render(request, 'student/registration.html', {'student_form': student_form})


def documentation(request, id):
    student = get_object_or_404(Student, pk=id)
    registration_form = create_student_registration_file(id)
    residence_form = create_residence_declaration_file(id)

    documents = False
    status = False
    observations = False

    try:
        documents = StudentDocuments.objects.get(student=id)
        status = DocumentStatus.objects.get(student=id)
        observations = DocumentObservation.objects.get(student=id)

    except StudentDocuments.DoesNotExist:
        documents = False
    except DocumentStatus.DoesNotExist:
        status = False
    except DocumentObservation.DoesNotExist:
        observations = False

    data = {
        'status': status,
        'observations': observations,
        'documents': documents,
        'student': student
    }

    return render(request, 'student/documentation.html', data)


def upload_student_document(request):
    if request.method == "POST":
        student_id = request.POST["student"]
        file_list = request.FILES

        print(Back.BLUE, "==>> student_documents: ", file_list)

        try:
            documents = StudentDocuments.objects.get(student=student_id)

            student_documents = StudentDocumentsForm(
                request.POST, request.FILES, instance=documents)

        except StudentDocuments.DoesNotExist:
            student_documents = StudentDocumentsForm(
                request.POST, request.FILES)

        if student_documents.is_valid():
            student_documents.save()

            student = get_object_or_404(Student, pk=student_id)

            status = DocumentStatus.objects.get_or_create(student=student)

            messages.success(request, 'Documento salvo com sucesso!')
            return redirect('/student/documentation/' + str(student_id))
        else:
            messages.error(request, 'Erro ao salvar os documentos!')
            print(Back.RED, "==>> class_form: ",
                  student_documents.errors.as_json())

            return redirect('/student/documentation/' + str(student_id))
    else:
        return redirect('/student/documentation/' + str(student_id))


def create_student_registration_file(id):
    student = get_object_or_404(Student, pk=id)
    print("==>> id: ", id)

    encoded_string = logo_tramite_base64()

    html = render_to_string('student/registration_form.html',
                            {'student': student, 'logo': encoded_string})

    pdf = pdfkit.from_string(html, "media/student/"+str(id) +
                             "/ficha_cadastral_tramite.pdf", configuration=CONFIG)

    return pdf


def create_residence_declaration_file(id):
    student = get_object_or_404(Student, pk=id)

    html = render_to_string(
        'student/residence_declaration_form.html', {'student': student})

    pdf = pdfkit.from_string(html, "media/student/"+str(id) +
                             "/declaracao_de_residencia.pdf", configuration=CONFIG)

    return pdf


def status_update(request, id):

    if request.method == "POST":
        try:
            documents = DocumentStatus.objects.get(student=id)

            status_doc = DocumentStatusForm(request.POST, instance=documents)

        except DocumentStatus.DoesNotExist:
            status_doc = DocumentStatusForm(request.POST)

        print("==>> status_doc: ", request.POST)

        if status_doc.is_valid():
            status_doc.save()

            messages.success(request, 'Status salvo com sucesso!')
            return redirect('/student/edit/' + str(id))
        else:
            messages.error(request, 'Erro ao salvar o status!')
            print(Back.RED, "==>> class_form: ",
                  status_doc.errors.as_json())

            return redirect('/student/edit/' + str(id))
    else:
        return redirect('/student/edit/' + str(id))


def save_observation(request, id):
    if request.method == "POST":
        updated_request = request.POST.copy()
        updated_request.update({'student': id})
        print(Back.RED, "==>> updated_request: ", updated_request)

        try:
            observations = DocumentObservation.objects.get(student=id)
            print(Back.BLUE, "==>> observations: ", observations)

            obs_form = DocumentObservationForm(
                updated_request, instance=observations)

        except DocumentObservation.DoesNotExist:
            obs_form = DocumentObservationForm(updated_request)

        if obs_form.is_valid():
            obs_form.save()

            messages.success(request, 'Observação salvo com sucesso!')
            return redirect('/student/edit/' + str(id))
        else:
            messages.error(request, 'Erro ao salvar o observação!')
            print(Back.RED, "==>> obs_form: ",
                  obs_form.errors.as_json())

            return redirect('/student/edit/' + str(id))
    else:
        return redirect('/student/edit/' + str(id))


def send_aprove_email(request, id):
    email = send_mail(
        'Teste',
        'Here is the message.',
        'peterson.paulo31@gmail.com',
        ['peterpaulodev@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse(email)
