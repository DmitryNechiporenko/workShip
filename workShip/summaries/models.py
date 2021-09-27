from django.contrib.auth.models import User
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.urls import reverse

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=255)
    job = models.CharField('Должность', max_length=255)
    city = models.CharField('Город', max_length=255)
    salary_min = models.CharField('Зарплата от', max_length=255)
    salary_max = models.CharField('Зарплата до', max_length=255)
    extra = models.TextField('Дополнительно', default='Без описания')
    image = models.ImageField(upload_to=image_directory_path, storage=image_storage, default='defaultuser.png')
    time_create = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    time_update = models.DateTimeField('Дата изменения', auto_now=True, null=True)
    is_published = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.name + " - " + self.job

    def get_absolute_url(self):
        return reverse('summaries_detail', kwargs={'summary_id': self.pk})

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'