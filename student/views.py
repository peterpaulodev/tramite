import os
from this import d
from colorama import Back
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from main.functions import clean_string, create_residence_declaration_file, create_student_registration_file, logo_tramite_base64
from student.models import DocumentObservation, DocumentStatus, Student, StudentDocuments
from django.contrib import messages
from student.forms import DocumentObservationForm, DocumentStatusForm, StudentDocumentsForm, StudentForm
from datetime import datetime
import pdfkit
from django.template.loader import render_to_string
from email.message import EmailMessage
from email.utils import formataddr
import smtplib

import importlib.util
import sys

# class module importation
spec = importlib.util.spec_from_file_location(
    "class.views", "./class/views.py")
_class = importlib.util.module_from_spec(spec)
sys.modules["module.name"] = _class
spec.loader.exec_module(_class)

CONFIG = pdfkit.configuration(wkhtmltopdf="./wkhtmltopdf/bin/wkhtmltopdf.exe")
# PROD: "/home/tramite/plataforma/wkhtmltopdf/bin/wkhtmltopdf.exe"


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
        status_form = DocumentStatusForm(instance=status)
    except DocumentStatus.DoesNotExist:
        status = False
        status_form = DocumentStatusForm()

    try:
        observations = DocumentObservation.objects.get(student=id)
        observation_form = DocumentObservationForm(instance=observations)
    except DocumentObservation.DoesNotExist:
        observations = False
        observation_form = DocumentObservationForm()

    print(Back.RED, "==>> observation_form: ", observations)

    data = {
        'student': student,
        'status': status,
        'observation_form': observation_form,
        'documents': documents,
        'status_form': status_form,
        'student_form': student_form,
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

        birth_date = datetime.strptime(updated_request['birth_date'], "%d/%m/%Y")
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


def status_update(request, id):

    if request.method == "POST":
        try:
            status = DocumentStatus.objects.get(student=id)

            status_form = DocumentStatusForm(request.POST, instance=status)

        except DocumentStatus.DoesNotExist:
            status_form = DocumentStatusForm(request.POST)

        print("==>> status_form: ", request.POST)

        if status_form.is_valid():
            status_form.save()

            messages.success(request, 'Status salvo com sucesso!')
            return redirect('/student/edit/' + str(id))
        else:
            messages.error(request, 'Erro ao salvar o status!')
            print(Back.RED, "==>> class_form: ",
                  status_form.errors.as_json())

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

            messages.success(request, 'Observação salva com sucesso!')
            return redirect('/student/edit/' + str(id))
        else:
            messages.error(request, 'Erro ao salvar o observação!')
            print(Back.RED, "==>> obs_form: ",
                  obs_form.errors.as_json())

            return redirect('/student/edit/' + str(id))
    else:
        return redirect('/student/edit/' + str(id))


EMAIL_ADDRESS = 'peterson.paulo31@gmail.com'
EMAIL_PASSWORD = 'teste'


def send_pending_email(request, id):
    student = get_object_or_404(Student, pk=id)
    msg = EmailMessage()
    msg['Subject'] = 'Documentação pendente...'
    msg['From'] = formataddr(('Trâmite Aéreo', EMAIL_ADDRESS))
    msg['To'] = 'peterpaulodev@gmail.com'
    body = '''
        Prezado(a) Aluno!

        Informamos que sua inscrição no curso AVSEC já está em andamento porém ainda constam pendências para regularizar.
        Pedimos que verifique os campos informados na Plataforma e anexe a documentação pendente para análise.
    '''
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    messages.success(request, 'Email enviado com sucesso!')

    return redirect('/student/edit/' + str(id))


def send_aprove_email(request, id):
    student = get_object_or_404(Student, pk=id)
    msg = EmailMessage()
    msg['Subject'] = 'Documentação aprovada!'
    msg['From'] = formataddr(('Trâmite Aéreo', EMAIL_ADDRESS))
    msg['To'] = 'peterpaulodev@gmail.com'
    body = '''
        Prezado(a) Aluno!

        Informamos que sua incrição no Curso AVSEC está confirmada e sua documentação está regular.

        Segue abaixo informações sobre o Curso: AVSEC

        Período: (data inicial) a (data final)
        Local do Curso:
        Nome do Instrutor:
    '''
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    messages.success(request, 'Email enviado com sucesso!')

    return redirect('/student/edit/' + str(id))


def link_in_class(request, id):
    if request.method == "POST":
        selected_class_id = request.POST['classes_name']
        print(Back.RED, "==>> selected_class_id: ", type(selected_class_id))

        if not selected_class_id:
            classes_instance = None
            messages.info(request, 'Atenção! O Vínculo ao curso foi removido.')
        else:
            classes_instance = _class.return_self_instance(selected_class_id)
            messages.success(request, 'Vínculo criado com sucesso!')

        student = Student.objects.get(pk=id)
        student.classes = classes_instance
        student.save()

    return redirect('/student/edit/' + str(id))
