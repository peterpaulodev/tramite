from dataclasses import fields
from django import forms
from .models import DocumentObservation, DocumentStatus, Student, StudentDocuments
from colorama import Fore, Back, Style


class StudentForm(forms.ModelForm):
    YESNO_CHOICES = [
        ('yes', 'Sim'),
        ('no', 'Não')
    ]

    aviation_work = forms.ChoiceField(choices=YESNO_CHOICES, widget=forms.RadioSelect)
    avsec_work = forms.ChoiceField(choices=YESNO_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Student
        fields = '__all__'


class StudentDocumentsForm(forms.ModelForm):

    class Meta:
        model = StudentDocuments
        fields = '__all__'


class DocumentStatusForm(forms.ModelForm):

    class Meta:
        model = DocumentStatus
        fields = '__all__'


class DocumentObservationForm(forms.ModelForm):

    class Meta:
        model = DocumentObservation
        fields = '__all__'
