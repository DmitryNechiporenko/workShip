from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

image_storage = FileSystemStorage(
    # Physical file location ROOT
    location=u'{0}/education/'.format(settings.MEDIA_ROOT),
    # Url for file
    base_url=u'{0}education/'.format(settings.MEDIA_URL),
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


class Study(models.Model):
    title = models.CharField('Название', max_length=255)
    first_price = models.IntegerField('Первичное обучение')
    secord_price = models.IntegerField('Повторное обучение')
    task = models.TextField('Задача', default='Без описания')
    education_forms_list = (('Дистанционно', 'Дистанционно'), ('Лекции', 'Лекции'), ('Семинары', 'Семинары'), ('Видеообучение', 'Видеообучение'), ('Тренинг', 'Тренинг'), ('Стажировка', 'Стажировка'), ('Производственный инструктаж', 'Производственный инструктаж'))
    education_form = models.CharField('Форма обучения', max_length=255, choices=education_forms_list)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Образовательная деятельность'
        verbose_name_plural = 'Образовательная деятельность'


class StudyResponses(models.Model):
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    phone = models.CharField('Телефон', max_length=15)
    email = models.EmailField('Email',max_length=50)

    def __str__(self):
        return self.created_at.strftime('%Y/%m/%d %H:%M') + " - " + self.name + " " + self.surname + " - " + self.study.title

    class Meta:
        verbose_name = 'Отклики на обучение'
        verbose_name_plural = 'Отклики на обучение'
        ordering = ['-created_at']

