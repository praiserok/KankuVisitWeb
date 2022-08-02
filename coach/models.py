from django.db import models
from django.urls import reverse
from belt.models import Belt
from slugify import slugify


class Coach(models.Model):

    first_name = models.CharField('Імя', max_length=20)
    last_name = models.CharField('Прізвище', max_length=25)
    surname = models.CharField('По батькові', max_length=20, blank=True)
    email = models.EmailField('Email', unique=True)
    # password = models.CharField('Пароль', max_length=128, blank=True)
    dateBirth = models.DateField('Дата народження', blank=True, null=True)
    telephone = models.IntegerField('Номер телефону', blank=True)
    telephone2 = models.IntegerField('Номер телефону 2', blank=True, null=True)
    belts = models.ForeignKey(Belt,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    information = models.TextField('Інформація про тренера', blank=True)
    # photo = models.ImageField('Фото', upload_to='coach/photo/%Y/%m/', blank=True)
    is_active = models.BooleanField('Тренує?', default=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name + '-' +
                            self.first_name)
        super(Coach, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренери'
        ordering = ['-is_active', 'last_name']

    def get_absolute_url(self):
        return reverse('coach')
        # ("coach-edit", kwargs={"coach_id": self.pk})
