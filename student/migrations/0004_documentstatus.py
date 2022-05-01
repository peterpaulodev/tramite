# Generated by Django 4.0.3 on 2022-04-29 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_studentdocuments_criminal_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_form', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('identity', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('criminal', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('basic_avsec_certificate', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('cnv', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('pilot_license', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('forwarding_in_service', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('work_card', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('avsec_certificate', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('certified_high_school', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('proof_of_address', models.CharField(blank=True, choices=[('APROVADO', 'Documento aprovado'), ('PENDENTE', 'Aguardando aprovação'), ('RECUSADO', 'Documento recusado')], max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.student')),
            ],
        ),
    ]
