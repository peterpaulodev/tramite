# Generated by Django 4.0.1 on 2022-03-25 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instructor', '0001_initial'),
        ('class', '0005_rename_class_classes'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='instructor.instructor'),
        ),
    ]
