# Generated by Django 4.0.3 on 2022-04-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='classes',
            name='anac_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='classes',
            name='zipcode',
            field=models.CharField(max_length=255),
        ),
    ]
