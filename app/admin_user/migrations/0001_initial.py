# Generated by Django 2.0.2 on 2018-03-08 12:05

import admin_user.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=128, unique=True, verbose_name='email')),
                ('_is_staff', models.BooleanField(default=False)),
                ('_is_active', models.BooleanField(default=True)),
                ('_is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', admin_user.models.MyUserManager()),
            ],
        ),
    ]