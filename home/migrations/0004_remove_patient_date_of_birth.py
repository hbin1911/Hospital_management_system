# Generated by Django 4.1.5 on 2023-02-25 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='date_of_birth',
        ),
    ]
