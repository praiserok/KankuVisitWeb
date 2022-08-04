from django.db import models
from django.urls import reverse
from group.models import Group
from django.utils.dateformat import DateFormat, TimeFormat
from slugify import slugify
import random


class TimetableDays(models.Model):

    days = models.CharField(max_length=15)

    def __str__(self):
        return self.days

    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дні тиждня'


class Timetable(models.Model):

    days = models.ManyToManyField(TimetableDays, blank=True)
    timeStart = models.TimeField('Час початку')
    timeFinish = models.TimeField('Час завершення')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):
        formatted_time = TimeFormat(self.timeStart)
        formatted_time_finish = TimeFormat(self.timeFinish)

        return str(self.days.all()) + ' - ' + str(formatted_time.format('H:i')) + '-'+str(formatted_time_finish.format('H:i'))

    def save(self, *args, **kwargs):

        self.slug = slugify('Rozklad' + str(self.group) +
                            str(random.randint(10000, 99999)))
        super(Timetable, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Графік'
        verbose_name_plural = 'Графіки'

    def get_absolute_url(self):
        return reverse('timetable')
