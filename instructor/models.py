from pyexpat import model
from django.db import models

# Create your models here.
class Instructor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    cpf = models.IntegerField()
    rg = models.IntegerField()
    primary_phone = models.IntegerField()
    secondary_phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InstructorDocuments(models.Model):
    identity = models.CharField(max_length=255)
    residence = models.CharField(max_length=255)
    criminal = models.CharField(max_length=255)
    curriculum = models.CharField(max_length=255)
    interview_quests = models.CharField(max_length=255)
    exams = models.CharField(max_length=255)
    tests = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name