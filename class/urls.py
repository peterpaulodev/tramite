from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('attendance_list', views.attendance_list, name='attendance_list'),
    path('attendance_list_export', views.attendance_list_export, name='attendance_list_export'),
    path('class_name', views.class_name_create, name='class_name'),
]
