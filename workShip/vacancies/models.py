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


class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Должность', max_length=255)
    salary = models.CharField('Зарплата', max_length=255)
    vessel_type = models.CharField('Тип судна', max_length=255, default="")
    date_start = models.DateField('Дата посадки')
    landing = models.CharField('Место посадки', max_length=255, default="")
    contract_term = models.CharField('Срок контракта', max_length=255, default="")
    image = models.ImageField(verbose_name='Изображение', upload_to=image_directory_path, storage=image_storage, default='defaultuser.png')
    time_create = models.DateTimeField('Дата создания', auto_now_add=True, null=True)
    time_update = models.DateTimeField('Дата изменения', auto_now=True, null=True)
    is_published = models.BooleanField('Публикация', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('vacancies_detail', kwargs={'vacancy_id': self.pk})

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-time_create', 'title']