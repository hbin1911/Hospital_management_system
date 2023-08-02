# Generated by Django 4.1.5 on 2023-03-24 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_address1_doctor_addresss_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomnumber', models.IntegerField()),
                ('roomtype', models.CharField(max_length=50)),
                ('patientname', models.CharField(max_length=100)),
                ('allotmentdte', models.DateField(auto_now_add=True)),
                ('dischargedte', models.DateField(auto_now_add=True)),
                ('docname', models.CharField(max_length=100)),
            ],
        ),
    ]
