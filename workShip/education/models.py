from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/summaries/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}summaries/'.format(settings.MEDIA_URL),
)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<filename>
    return u'{0}'.format(filename)


class Practice(models.Model):
    title = models.CharField('Название', max_length=255)
    salary = models.CharField('Зарплата', max_length=255)
    date_start = models.DateField()
    date_end = models.DateField()
    company = models.CharField('Компания', max_length=255)
    description = models.TextField('Описание', default='Без описания')
    image = models.ImageField(upload_to=image_directory_path, storage=image_storage, default='static/defaultuser.png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Практика'
        verbose_name_plural = 'Практика'


