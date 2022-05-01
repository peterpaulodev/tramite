# Generated by Django 4.0.3 on 2022-04-27 19:59

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('primary_phone', models.CharField(max_length=100)),
                ('secondary_phone', models.CharField(max_length=100)),
                ('birth_date', models.DateTimeField()),
                ('cpf', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=100)),
                ('issuing_agency', models.CharField(max_length=100)),
                ('scholarity', models.CharField(max_length=100)),
                ('working_company_name', models.CharField(max_length=100)),
                ('naturalness', models.CharField(max_length=255)),
                ('nationality', models.CharField(max_length=255)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('avsec_work', models.BooleanField(default=False)),
                ('aviation_work', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('neigh', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('uf', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('classes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='class.classes')),
            ],
        ),
        migrations.CreateModel(
            name='StudentDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_form', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('identity', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('criminal', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('basic_avsec_certificate', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('cnv', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('pilot_license', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('forwarding_in_service', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('work_card', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('avsec_certificate', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('certified_high_school', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('proof_of_address', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('criminal_record', models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='student.student')),
            ],
        ),
    ]
