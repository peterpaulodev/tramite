from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('registration', views.registration, name='registration'),
    path('pre_register_validation', views.pre_register_validation, name='pre_register_validation'),
    path('documentation/<int:id>', views.documentation, name='documentation'),
    path('upload_student_document', views.upload_student_document, name='upload_student_document'),
    path('status_update/<int:id>', views.status_update, name='status_update'),
    path('save_observation/<int:id>', views.save_observation, name='save_observation'),
    path('send_aprove_email/<int:id>', views.send_aprove_email, name='send_aprove_email'),
    path('send_pending_email/<int:id>', views.send_pending_email, name='send_pending_email'),
    path('link_in_class/<int:id>', views.link_in_class, name='link_in_class'),
]
