# Generated by Django 2.0.2 on 2018-03-08 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='_is_active',
            new_name='is_active',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='_is_admin',
            new_name='is_admin',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='_is_staff',
            new_name='is_staff',
        ),
    ]