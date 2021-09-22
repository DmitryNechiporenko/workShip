# Generated by Django 3.1.7 on 2021-09-22 15:57

import django.core.files.storage
from django.db import migrations, models
import vacancies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255, verbose_name='Компания')),
                ('title', models.CharField(max_length=255, verbose_name='Должность')),
                ('salary', models.CharField(max_length=255, verbose_name='Зарплата')),
                ('vessel_type', models.CharField(default='', max_length=255, verbose_name='Тип судна')),
                ('date_start', models.DateField(verbose_name='Дата посадки')),
                ('landing', models.CharField(default='', max_length=255, verbose_name='Место посадки')),
                ('contract_term', models.CharField(default='', max_length=255, verbose_name='Срок контракта')),
                ('image', models.ImageField(default='defaultuser.png', storage=django.core.files.storage.FileSystemStorage(base_url='/media/summaries/', location='F:\\Workspace\\PyCharm projects\\workShip django\\workShip\\media/summaries/'), upload_to=vacancies.models.image_directory_path, verbose_name='Изображение')),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-time_create', 'title'],
            },
        ),
    ]
