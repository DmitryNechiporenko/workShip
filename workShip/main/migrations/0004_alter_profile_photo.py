# Generated by Django 3.2.7 on 2021-09-22 07:44

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210922_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='defaultuser.png', null=True, upload_to=main.models.image_directory_path, verbose_name='Изображение профиля'),
        ),
    ]