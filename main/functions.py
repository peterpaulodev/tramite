import base64
import re
import pdfkit


def clean_string(value):
    return re.sub('[^A-Za-z0-9]+', '', value)


def document_status_name(status):
    new_status = 'Aguardando Aprovação'

    if status == 'RECUSADO':
        new_status = 'Documento recusado'
    elif status == 'APROVADO':
        new_status = 'Documento aprovado'

    return new_status

def logo_tramite_base64():
    with open("static/dist/img/logo-tramite.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    return encoded_string.decode('utf-8')