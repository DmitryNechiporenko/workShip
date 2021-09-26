import datetime

from django.contrib.auth.models import User, AbstractUser
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/profile/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}profile/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<filename>
    return u'{0}'.format(filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_company = models.BooleanField(verbose_name='Это компания', default=False)
    company_name = models.CharField(verbose_name='Название компании', max_length=255, null=True, blank=True)
    patronymic = models.CharField(verbose_name='Отчество', max_length=255, null=True)
    photo = models.ImageField(verbose_name='Изображение профиля', upload_to=image_directory_path,
                              default='defaultuser.png', null=True, blank=True)
    country = models.CharField(verbose_name='Страна', max_length=100, blank=False)
    city = models.CharField(verbose_name='Город', max_length=100, blank=False)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=12, null=True)
    birthdate = models.DateField(verbose_name='Дата рождения', default=datetime.date.today, null=True)


class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(verbose_name='Название компании', max_length=255)
    logo = models.ImageField(verbose_name='Логотип компании', upload_to=image_directory_path, default='defaultuser.png', blank=True, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    about = models.TextField(verbose_name='О компании')
    contact_patronymic = models.CharField(verbose_name='Отчество', max_length=255)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=12)


#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)


#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
