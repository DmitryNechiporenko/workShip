# Generated by Django 3.1.7 on 2021-09-22 15:57

import django.core.files.storage
from django.db import migrations, models
import seaman.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeamanBlank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('file', models.FileField(default='static/defaultuser.png', storage=django.core.files.storage.FileSystemStorage(base_url='/media/seaman/blanks/', location='F:\\Workspace\\PyCharm projects\\workShip django\\workShip\\media/seaman/blanks/'), upload_to=seaman.models.blank_directory_path)),
            ],
            options={
                'verbose_name': 'Дипломный сектор',
                'verbose_name_plural': 'Дипломный сектор',
            },
        ),
        migrations.CreateModel(
            name='SeamanDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(default='static/defaultuser.png', storage=django.core.files.storage.FileSystemStorage(base_url='/media/seaman/', location='F:\\Workspace\\PyCharm projects\\workShip django\\workShip\\media/seaman/'), upload_to=seaman.models.image_directory_path)),
            ],
            options={
                'verbose_name': 'Документы морякам',
                'verbose_name_plural': 'Документы морякам',
            },
        ),
    ]
