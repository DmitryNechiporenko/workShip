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

class Summary(models.Model):
    name = models.CharField('Название', max_length=255)
    job = models.CharField('Должность', max_length=255)
    city = models.CharField('Город', max_length=255)
    salary_min = models.CharField('Зарплата от', max_length=255)
    salary_max = models.CharField('Зарплата до', max_length=255)
    extra = models.TextField('Дополнительно', default='Без описания')
    image = models.ImageField(upload_to=image_directory_path, storage=image_storage, default='static/defaultuser.png')

    def __str__(self):
        return self.name + " - " + self.job

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'