from dataclasses import fields
from django import forms
from .models import Classes, ClassesName
import time

class ClassesForm(forms.ModelForm):

    class Meta:
        model = Classes
        fields = '__all__'

        def clean_intial_date(self):
            data = self.cleaned_data

            first_date = data['initial_date']
            print("==>> first_date: ", first_date)
            second_date = data['finish_date']
            print("==>> second_date: ", second_date)

            formatted_date1 = time.strptime(first_date, "%d/%m/%Y")
            formatted_date2 = time.strptime(second_date, "%d/%m/%Y")

            print(formatted_date1 > formatted_date2)

            return False

class ClassesNameForm(forms.ModelForm):
    class Meta:
        model = ClassesName
        fields = '__all__'