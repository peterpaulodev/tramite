# Generated by Django 4.0.3 on 2022-05-19 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_classesname_remove_classes_name_classes_name_class'),
        ('student', '0002_student_classes_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='classes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='class.classes'),
        ),
    ]
