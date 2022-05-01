from dataclasses import fields
from django import forms
from .models import Student, StudentDocuments
from colorama import Fore, Back, Style

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class StudentDocumentsForm(forms.ModelForm):

    class Meta:
        model = StudentDocuments
        fields = '__all__'