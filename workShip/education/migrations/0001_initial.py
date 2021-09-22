# Generated by Django 3.1.7 on 2021-09-22 15:57

import django.core.files.storage
from django.db import migrations, models
import education.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('salary', models.CharField(max_length=255, verbose_name='Зарплата')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('company', models.CharField(max_length=255, verbose_name='Компания')),
                ('description', models.TextField(default='Без описания', verbose_name='Описание')),
                ('image', models.ImageField(default='static/defaultuser.png', storage=django.core.files.storage.FileSystemStorage(base_url='/media/summaries/', location='F:\\Workspace\\PyCharm projects\\workShip django\\workShip\\media/summaries/'), upload_to=education.models.image_directory_path)),
            ],
            options={
                'verbose_name': 'Практика',
                'verbose_name_plural': 'Практика',
            },
        ),
    ]
