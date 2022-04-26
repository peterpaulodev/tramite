from pyexpat import model
from django.db import models

# Create your models here.
class Classes(models.Model):
    anac_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    number = models.IntegerField()
    neigh = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    initial_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    instructor = models.ForeignKey("instructor.Instructor", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name