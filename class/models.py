from pyexpat import model
from django.db import models

# Create your models here.
class Classes(models.Model):
    PERIOD_CHOICES = [
        ('MANHA', 'Manhã'),
        ('TARDE', 'Tarde'),
        ('NOITE', 'Noite'),
        ('MANHA/TARDE', 'Manhã/Tarde'),
        ('TARDE/NOITE', 'Tarde/Noite'),
        ('MANHA/TARDE/NOITE', 'Manhã/Tarde/Noite'),
        ('MANHA/NOITE', 'Manhã/Noite'),
    ]

    anac_id = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    number = models.IntegerField()
    neigh = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    period = models.CharField(max_length=255, choices=PERIOD_CHOICES, null=True)
    initial_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    instructor = models.ForeignKey("instructor.Instructor", on_delete=models.SET_NULL, null=True)
    name_class = models.ForeignKey("ClassesName", on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        context = f'[{self.anac_id}] {self.name_class.name}'
        return context

class ClassesName(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name