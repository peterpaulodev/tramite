from dataclasses import fields
from django import forms
from .models import Classes


class ClassesForm(forms.ModelForm):

    class Meta:
        model = Classes
        fields = ('anac_id',
                  'name',
                  'address',
                  'zipcode',
                  'number',
                  'neigh',
                  'city',
                  'initial_date',
                  'finish_date')
