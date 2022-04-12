# Generated by Django 4.0.3 on 2022-03-23 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('zipcode', models.IntegerField(max_length=8)),
                ('number', models.IntegerField(max_length=100)),
                ('neigh', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('initial_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]