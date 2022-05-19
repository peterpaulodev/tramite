from django.db import models

from main.functions import document_status_name

# Create your models here.
class Student(models.Model):
    UF_CHOICES = [
        ("AC", 'Acre'),
        ("AL", 'Alagoas'),
        ("AP", 'Amapá'),
        ("AM", 'Amazonas'),
        ("BA", 'Bahia'),
        ("CE", 'Ceará'),
        ("DF", 'Distrito Federal'),
        ("ES", 'Espirito Santo'),
        ("GO", 'Goiás'),
        ("MA", 'Maranhão'),
        ("MS", 'Mato Grosso do Sul'),
        ("MT", 'Mato Grosso'),
        ("MG", 'Minas Gerais'),
        ("PA", 'Pará'),
        ("PB", 'Paraíba'),
        ("PR", 'Paraná'),
        ("PE", 'Pernambuco'),
        ("PI", 'Piauí'),
        ("RJ", 'Rio de Janeiro'),
        ("RN", 'Rio Grande do Norte'),
        ("RS", 'Rio Grande do Sul'),
        ("RO", 'Rondônia'),
        ("RR", 'Roraima'),
        ("SC", 'Santa Catarina'),
        ("SP", 'São Paulo'),
        ("SE", 'Sergipe'),
        ("TO", 'Tocantins'),
    ]

    SCHOLARITY_CHOICES = [
        ("Ensino Fundamental", 'Ensino Fundamental completo'),
        ("Ensino Medio", 'Ensino Medio completo'),
        ("Ensino Superior", 'Ensino Superior completo'),
        ("Pos Graduacao", 'Pós-Graduação completo'),
    ]

    ISSUING_CHOICES = [
        ('SSP', 'SSP - Secretaria de Segurança Pública'),
        ('PM', 'PM - Polícia Militar'),
        ('PC', 'PC - Policia Civil'),
        ('CNT', 'CNT - Carteira Nacional de Habilitação'),
        ('DIC', 'DIC - Diretoria de Identificação Civil'),
        ('CTPS', 'CTPS - Carteira de Trabaho e Previdência Social'),
        ('FGTS', 'FGTS - Fundo de Garantia do Tempo de Serviço'),
        ('IFP', 'IFP - Instituto Félix Pacheco'),
        ('IPF', 'IPF - Instituto Pereira Faustino'),
        ('IML', 'IML - Instituto Médico-Legal'),
        ('MTE', 'MTE - Ministério do Trabalho e Emprego'),
        ('MMA', 'MMA - Ministério da Marinha'),
        ('MAE', 'MAE - Ministério da Aeronáutica'),
        ('MEX', 'MEX - Ministério do Exército'),
        ('POF', 'POF - Polícia Federal'),
        ('POM', 'POM - Polícia Militar'),
        ('SES', 'SES - Carteira de Estrangeiro'),
        ('SJS', 'SJS - Secretaria da Justiça e Segurança'),
        ('SJTS', 'SJTS - Secretaria da Justiça do Trabalho e Segurança'),
        ('ZZZ', 'ZZZ - Outros (inclusive exterior)'),
    ]

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    primary_phone = models.CharField(max_length=100)
    secondary_phone = models.CharField(max_length=100, null=True, blank=True)

    birth_date = models.DateTimeField()
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    issuing_agency = models.CharField(max_length=100, choices=ISSUING_CHOICES)

    scholarity = models.CharField(max_length=100, choices=SCHOLARITY_CHOICES)
    working_company_name = models.CharField(max_length=100)

    naturalness = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)

    mother_name = models.CharField(max_length=100, null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)

    avsec_work = models.CharField(max_length=100, null=True, blank=True)
    aviation_work = models.CharField(max_length=100, null=True, blank=True)

    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    number = models.IntegerField()
    neigh = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    uf = models.CharField(max_length=255, choices=UF_CHOICES)
    complement = models.CharField(max_length=255, null=True, blank=True)

    ready_documents = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    in_class = models.ForeignKey("class.Classes", on_delete=models.SET_NULL, null=True, name='classes')

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    return '/'.join(['student', str(instance.student.id), filename])

class StudentDocuments(models.Model):
    registration_form = models.FileField(name='registration_form', upload_to=user_directory_path, null=True, blank=True)
    identity = models.FileField(name='identity', upload_to=user_directory_path, null=True, blank=True)
    cnh = models.FileField(name='cnh', upload_to=user_directory_path, null=True, blank=True)
    criminal = models.FileField(name='criminal', upload_to=user_directory_path, null=True, blank=True)
    distribution_criminal = models.FileField(name='distribution_criminal', upload_to=user_directory_path, null=True, blank=True)
    basic_avsec_certificate = models.FileField(name='basic_avsec_certificate', upload_to=user_directory_path, null=True, blank=True)
    cnv = models.FileField(name='cnv', upload_to=user_directory_path, null=True, blank=True)
    pilot_license = models.FileField(name='pilot_license', upload_to=user_directory_path, null=True, blank=True)
    forwarding_in_service = models.FileField(name='forwarding_in_service', upload_to=user_directory_path, null=True, blank=True)
    work_card = models.FileField(name='work_card', upload_to=user_directory_path, null=True, blank=True)
    avsec_certificate = models.FileField(name='avsec_certificate', upload_to=user_directory_path, null=True, blank=True)
    certified_high_school = models.FileField(name='certified_high_school', upload_to=user_directory_path, null=True, blank=True)
    proof_of_address = models.FileField(name='proof_of_address', upload_to=user_directory_path, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    student = models.OneToOneField("Student", on_delete=models.SET_NULL, null=True, name='student')

    def __str__(self):
        return self.student.name

class DocumentStatus(models.Model):

    STATUS_CHOICES = [
        ('APROVADO', 'Documento aprovado'),
        ('PENDENTE', 'Aguardando aprovação'),
        ('RECUSADO', 'Documento não aceito')
    ]

    registration_form = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    identity = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    cnh = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    criminal = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    distribution_criminal = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    basic_avsec_certificate = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    cnv = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    pilot_license = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    forwarding_in_service = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    work_card = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    avsec_certificate = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    certified_high_school = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)
    proof_of_address = models.CharField(max_length=100, choices=STATUS_CHOICES, default='PENDENTE', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    student = models.OneToOneField("Student", on_delete=models.SET_NULL, null=True, name='student')

    def __str__(self):
        return self.student.name

    def registration_form_name(self):
        return document_status_name(self.registration_form)

    def identity_name(self):
        return document_status_name(self.identity)

    def cnh_name(self):
        return document_status_name(self.cnh)

    def criminal_name(self):
        return document_status_name(self.criminal)

    def distribution_criminal_name(self):
        return document_status_name(self.distribution_criminal)

    def basic_avsec_certificate_name(self):
        return document_status_name(self.basic_avsec_certificate)

    def cnv_name(self):
        return document_status_name(self.cnv)

    def work_card_name(self):
        return document_status_name(self.work_card)

    def forwarding_in_service_name(self):
        return document_status_name(self.forwarding_in_service)

    def avsec_certificate_name(self):
        return document_status_name(self.avsec_certificate)

    def certified_high_school_name(self):
        return document_status_name(self.certified_high_school)

    def proof_of_address_name(self):
        return document_status_name(self.proof_of_address)

class DocumentObservation(models.Model):

    registration_form_observation = models.TextField(null=True, blank=True)
    identity_observation = models.TextField(null=True, blank=True)
    cnh_observation = models.TextField(null=True, blank=True)
    criminal_observation = models.TextField(null=True, blank=True)
    distribution_criminal_observation = models.TextField(null=True, blank=True)
    basic_avsec_certificate_observation = models.TextField(null=True, blank=True)
    cnv_observation = models.TextField(null=True, blank=True)
    pilot_license_observation = models.TextField(null=True, blank=True)
    forwarding_in_service_observation = models.TextField(null=True, blank=True)
    work_card_observation = models.TextField(null=True, blank=True)
    avsec_certificate_observation = models.TextField(null=True, blank=True)
    certified_high_school_observation = models.TextField(null=True, blank=True)
    proof_of_address_observation = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    student = models.OneToOneField("Student", on_delete=models.SET_NULL, null=True, name='student')

    def __str__(self):
        return self.student.name