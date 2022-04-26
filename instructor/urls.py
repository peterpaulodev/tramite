from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('upload_instructor_document', views.upload_instructor_document, name='upload_instructor_document'),
    path('ready_documents/<int:id>/<int:ready>', views.ready_documents, name='ready_documents'),
]
