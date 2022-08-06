from django.db import models
from django.urls import reverse
from coach.models import Coach
from slugify import slugify
from django.utils.dateformat import DateFormat, TimeFormat
import random


class School(models.Model):
    name = models.CharField('Назва', max_length=35)
    city = models.CharField('Місто', max_length=20)
    adress = models.CharField('Вулиця', max_length=35)
    coach = models.ForeignKey(Coach,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    is_active = models.BooleanField('Працює?', default=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + '-' +
                            self.adress)
        super(School, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школи'

    def get_absolute_url(self):
        return reverse('school')


class Group(models.Model):

    name = models.CharField('Імя', max_length=20)
    costMoon = models.IntegerField('Вартість місяця', blank=True, null=True)
    costTraining = models.IntegerField(
        'Вартість 1-го тренування', blank=True, null=True)
    school = models.ForeignKey(School,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)

    coach = models.ForeignKey(Coach,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):

        if self.school:
            groupSchool = str(self.school) + ' - ' + str(self.name)
            return groupSchool
        else:
            print(self.school)
            return 'Не вибрано зал - ' + self.name
        # school = self.name self.school

    def save(self, *args, **kwargs):
        if(self.school == None):
            randoms = str(random.randint(10000, 99999))
            self.slug = slugify(self.name + '-' + randoms)
        else:
            self.slug = slugify(self.name + '-' + str(self.school))
        super(Group, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'

    def get_absolute_url(self):
        return reverse('group')


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
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=False,
                              null=False)
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
