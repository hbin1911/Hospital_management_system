# Generated by Django 4.1.5 on 2023-02-26 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_book_email_alter_book_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='address1',
            new_name='addresss',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='age1',
            new_name='agee',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='email1',
            new_name='emaill',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='gender1',
            new_name='genderr',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='phone1',
            new_name='phonee',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='roles1',
            new_name='roless',
        ),
    ]
