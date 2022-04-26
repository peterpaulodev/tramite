from dataclasses import fields
from django import forms
from .models import Instructor, InstructorDocuments
from main.functions import clean_string
from colorama import Fore, Back, Style

class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        fields = '__all__'

    def clean(self):
            form_fields = self.cleaned_data

            print(Back.RED + ' -> ', self.errors)


            for field in form_fields:
                field = field
                print(Back.RED + "==>> field: ", field)

            print(Back.GREEN + ' -> ', form_fields)

            return form_fields


class InstructorDocumentsForm(forms.ModelForm):

    class Meta:
        model = InstructorDocuments
        fields = '__all__'