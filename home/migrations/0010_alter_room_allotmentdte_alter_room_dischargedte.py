# Generated by Django 4.1.5 on 2023-03-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='allotmentdte',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='room',
            name='dischargedte',
            field=models.CharField(max_length=50),
        ),
    ]