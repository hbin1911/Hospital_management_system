# Generated by Django 4.1.5 on 2023-03-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_room_allotmentdte_alter_room_dischargedte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.TextField(),
        ),
    ]