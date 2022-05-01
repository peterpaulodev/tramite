from this import d
from colorama import Back
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from main.functions import clean_string, logo_tramite_base64
from student.models import DocumentObservation, DocumentStatus, Student, StudentDocuments
from django.contrib import messages
from student.forms import StudentDocumentsForm, StudentForm
from datetime import datetime
import pdfkit
from student.models import Student
from django.template.loader import render_to_string
import base64

# Create your views here.
@login_required
def index(request):
    student = Student.objects.all()

    data = {
        'has_datatable': True,
        'student': student
    }

    return render(request, 'student/index.html', data)


@login_required
def edit(request, id):
    student = get_object_or_404(Student, pk=id)
    student_form = StudentForm(instance=student)

    try:
        documents = StudentDocuments.objects.get(
            student=id)

    except StudentDocuments.DoesNotExist:
        documents = False

    data = {
        'documents': documents,
        'student': student,
        'student_form': student_form
    }

    if request.method == 'POST':
        student_form = StudentDocuments(request.POST, instance=student)

        if student_form.is_valid():
            student_form.save()

            data['student_form'] = student_form
            messages.success(request, 'Instrutor editado com sucesso!')

            return render(request, 'student/edit.html', data)

        else:
            messages.error(request, 'Erro ao validar o cadastro de instrutor!')
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

                messages.success(request, 'Seja bem vindo! ' + student_form.data['name'])
                return redirect('/student/documentation/' + str(student_form.data['id']))

        else:
            print(Back.RED, "==>> student_form: ", student_form.errors.as_json())
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

            messages.success(request, 'Seja bem vindo! ' + student.name)
            return redirect('/student/documentation/' + str(student.id))
        except Student.DoesNotExist:
            messages.error(request, 'Não foi encontrado nenhum aluno com esses dados!')
            return redirect('/accounts/login')
    else:
        return render(request, 'student/registration.html', {'student_form': student_form})

def documentation(request, id):
    student = get_object_or_404(Student, pk=id)
    registration_form = create_student_registration_file(id)

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

            student_documents = StudentDocumentsForm(request.POST, request.FILES, instance=documents)

        except StudentDocuments.DoesNotExist:
            student_documents = StudentDocumentsForm(request.POST, request.FILES)

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

    config = pdfkit.configuration(
        wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    encoded_string = logo_tramite_base64()

    html = render_to_string('student/registration_form.html', {'student': student, 'logo': encoded_string})

    pdf = pdfkit.from_string(html, "media/student/"+str(id)+"/ficha_cadastral_tramite.pdf", configuration=config)

    return pdf
