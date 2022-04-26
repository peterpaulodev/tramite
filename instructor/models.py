from pyexpat import model
from colorama import Back
from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    primary_phone = models.CharField(max_length=100)
    secondary_phone = models.CharField(max_length=100)
    secondary_phone = models.CharField(max_length=100)
    ready_documents = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    return '/'.join(['documents', str(instance.instructor.id), filename])
class InstructorDocuments(models.Model):
    identity = models.FileField(name='identity', upload_to=user_directory_path, null=True, blank=True)
    residence = models.FileField(name='residence', upload_to=user_directory_path, null=True, blank=True)
    criminal = models.FileField(name='criminal', upload_to=user_directory_path, null=True, blank=True)
    curriculum = models.FileField(name='curriculum', upload_to=user_directory_path, null=True, blank=True)
    interview_quests = models.FileField(name='interview_quests', upload_to=user_directory_path, null=True, blank=True)
    exams = models.FileField(name='exams', upload_to=user_directory_path, null=True, blank=True)
    tests = models.FileField(name='tests', upload_to=user_directory_path, null=True, blank=True)
    scholar_history = models.FileField(name='scholar_history', upload_to=user_directory_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    instructor = models.OneToOneField("Instructor", on_delete=models.SET_NULL, null=True, name='instructor')

    def __str__(self):
        return self.instructor.name