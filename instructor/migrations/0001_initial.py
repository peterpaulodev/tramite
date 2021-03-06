# Generated by Django 4.0.3 on 2022-05-19 01:15

from django.db import migrations, models
import django.db.models.deletion
import instructor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=100)),
                ('rg', models.CharField(max_length=100)),
                ('primary_phone', models.CharField(max_length=100)),
                ('secondary_phone', models.CharField(max_length=100)),
                ('ready_documents', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InstructorDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.FileField(blank=True, null=True, upload_to=instructor.models.user_directory_path)),
                ('residence', models.FileField(blank=True, null=True, upload_to=instructor.models.user_directory_path)),
                ('criminal', models.FileField(blank=True, null=True, upload_to=instructor.models.user_directory_path)),
                ('curriculum', models.FileField(blank=True, null=True, upload_to=instructor.models.user_directory_path)),
                ('interview_quests', models.FileField(blank=True, null=True, upload_to=instructor.models.user_directory_path)),
                ('exams', models.FileField(blank=True, null=True, upload_to=instructor.models.user_directory_path)),
                ('tests', models.FileField(blank=True, null=True, upload_to=instructor.models.user_directory_path)),
                ('scholar_history', models.FileField(blank=True, null=True, upload_to=instructor.models.user_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('instructor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instructor.instructor')),
            ],
        ),
    ]
