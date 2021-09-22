# Generated by Django 3.2.7 on 2021-09-22 07:42

import datetime
from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210917_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='defaultuser.png', null=True, upload_to=main.models.image_directory_path, verbose_name='Изображение профиля'),
        ),
    ]