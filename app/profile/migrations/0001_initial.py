# Generated by Django 2.0.2 on 2018-03-15 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', versatileimagefield.fields.VersatileImageField(upload_to='media/images/avatart', verbose_name='Avatar')),
                ('background', versatileimagefield.fields.VersatileImageField(upload_to='media/images/background', verbose_name='Background')),
                ('about', models.CharField(max_length=2048)),
                ('website_url', models.URLField(max_length=256)),
                ('date_birth', models.DateField()),
                ('user_model', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
