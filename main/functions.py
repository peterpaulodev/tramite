from datetime import date, timedelta, datetime
import base64
import os
import re
from colorama import Back
from django.shortcuts import get_object_or_404
import pdfkit
from django.template.loader import render_to_string

import student.models

CONFIG = pdfkit.configuration(wkhtmltopdf="./wkhtmltopdf/bin/wkhtmltopdf.exe")


def clean_string(value):
    return re.sub('[^A-Za-z0-9]+', '', value)


def document_status_name(status):
    new_status = 'Aguardando Aprovação'

    if status == 'RECUSADO':
        new_status = 'Documento não aceito'
    elif status == 'APROVADO':
        new_status = 'Documento aprovado'

    return new_status


def class_period(period):

    if period == 'MANHA':
        new_period = 'Manhã'

    elif period == 'TARDE':
        new_period = 'Tarde'

    elif period == 'NOITE':
        new_period = 'Noite'

    elif period == 'MANHA/TARDE':
        new_period = 'Manhã/Tarde'

    elif period == 'TARDE/NOITE':
        new_period = 'Tarde/Noite'

    elif period == 'MANHA/TARDE/NOITE':
        new_period = 'Manhã/Tarde/Noite'

    elif period == 'MANHA/NOITE':
        new_period = 'Manhã/Noite'

    return new_period


def logo_tramite_base64():
    with open("static/dist/img/logo-tramite.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string.decode('utf-8')


def create_attendance_list_file(classes, id):
    _class = get_object_or_404(classes, pk=id)
    students = student.models.Student.objects.filter(classes=_class)

    encoded_string = logo_tramite_base64()
    student_count = 10

    dates = get_interval_date_list(_class.initial_date, _class.finish_date)
    print("==>> dates: ", dates)
    periods = _class.get_class_period().split('/')

    context = {
        'class': _class,
        'dates_realization': dates,
        'logo': encoded_string,
        'student_count': student_count,
        'periods': periods,
        'count_columns': len(periods) + 2,
        'student_count': len(students),
        'students': students,
    }

    html = render_to_string(
        'class/attendance_list.html', context)

    path = "media/classes/" + str(id) + "/lista_de_presença - curso " + _class.anac_id + ".pdf"

    pdf = pdfkit.from_string(html, path, configuration=CONFIG)

    return path

def create_rule_list_file(classes, id):
    _class = get_object_or_404(classes, pk=id)
    students = student.models.Student.objects.filter(classes=_class)

    encoded_string = logo_tramite_base64()

    context = {
        'class': _class,
        'logo': encoded_string,
        'students': students,
    }

    html = render_to_string(
        'class/rule_receive.html', context)

    path = "media/classes/" + str(id) + "/lista_de_recebimento_do_regulamento - curso " + _class.anac_id + ".pdf"

    pdf = pdfkit.from_string(html, path, configuration=CONFIG)

    return path


def create_student_registration_file(id):
    student_instance = get_object_or_404(student.models.Student, pk=id)

    encoded_string = logo_tramite_base64()

    html = render_to_string('student/registration_form.html',
                            {'student': student_instance, 'logo': encoded_string})

    pdf = pdfkit.from_string(html, "media/student/"+str(id) +
                             "/ficha_cadastral_tramite.pdf", configuration=CONFIG)

    return pdf


def create_residence_declaration_file(id):
    student_instance = get_object_or_404(student.models.Student, pk=id)

    html = render_to_string(
        'student/residence_declaration_form.html', {'student': student_instance})

    pdf = pdfkit.from_string(html, "media/student/"+str(id) +
                             "/declaracao_de_residencia.pdf", configuration=CONFIG)

    return pdf


def get_interval_date_list(initial_date, final_date):
    delta = final_date - initial_date

    date_list = []
    for i in range(delta.days + 1):
        day = initial_date + timedelta(days=i)
        date_list.append(day)

    date_list_str = [datetime.strftime(
        dt, format="%d/%m/%Y") for dt in date_list]

    return date_list_str
