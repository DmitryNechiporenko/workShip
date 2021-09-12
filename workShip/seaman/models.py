from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/seaman/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}seaman/'.format(settings.MEDIA_URL),
)

def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<filename>
    return u'{0}'.format(filename)


blank_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/seaman/blanks/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}seaman/blanks/'.format(settings.MEDIA_URL),
)


def blank_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/<filename>
    return u'{0}'.format(filename)


class SeamanDocument(models.Model):
    name = models.CharField('Название', max_length=255)
    image = models.ImageField(upload_to=image_directory_path, storage=image_storage, default='static/defaultuser.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документы морякам'
        verbose_name_plural = 'Документы морякам'


class SeamanBlank(models.Model):
    name = models.CharField('Название', max_length=255)
    file = models.FileField(upload_to=blank_directory_path, storage=blank_storage, default='static/defaultuser.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дипломный сектор'
        verbose_name_plural = 'Дипломный сектор'