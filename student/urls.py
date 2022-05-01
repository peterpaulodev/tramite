from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('registration', views.registration, name='registration'),
    path('pre_register_validation', views.pre_register_validation, name='pre_register_validation'),
    path('documentation/<int:id>', views.documentation, name='documentation'),
    path('upload_student_document', views.upload_student_document, name='upload_student_document'),
    # path('create_student_registration_file/<int:id>', views.create_student_registration_file, name='create_student_registration_file'),
]
