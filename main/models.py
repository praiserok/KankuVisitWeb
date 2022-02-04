from calendar import day_abbr
import email
from operator import truediv
from time import time
from tokenize import group
from unicodedata import name
from django.db import models

gradation = [(0, 'Білий пояс'), (10, '10 кю'), (9, '9 кю'), (8, '8 кю'),
             (7, '7 кю'), (6, '6 кю'), (5, '5 кю'), (4, '4 кю'), (3, '3 кю'),
             (2, '2 кю'), (1, '1 кю'), (11, '1 дан'), (12, '2 дан'),
             (13, '3 дан'), (14, '4 дан'), (15, '5 дан'), (16, '6 дан'),
             (17, '7 дан'), (18, '8 дан'), (19, '9 дан')]


class Task(models.Model):
    title = models.CharField('Назва', max_length=50)
    task = models.TextField('Опис')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'


class Coach(models.Model):

    first_name = models.CharField('Імя', max_length=20)
    last_name = models.CharField('Прізвище', max_length=25)
    surname = models.CharField('По батькові', max_length=20, blank=True)
    email = models.EmailField('Email', unique=True)
    password = models.CharField('Пароль', max_length=128, blank=True)
    dateBirth = models.DateField('Дата народження')
    telephone = models.IntegerField('Номер телефону')
    telephone2 = models.IntegerField('Номер телефону 2', blank=True, null=True)
    belt = models.SmallIntegerField('Рівень поясу',
                                    choices=gradation,
                                    default=0,
                                    null=True)
    information = models.TextField('Інформація про тренера')
    photo = models.ImageField('Фото', blank=True)
    is_active = models.BooleanField('Тренує?', default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренери'


class School(models.Model):
    name = models.CharField('Назва', max_length=35)
    city = models.CharField('Місто', max_length=20)
    adress = models.CharField('Вулиця', max_length=35)
    is_active = models.BooleanField('Працює?', default=True)
    coach = models.ForeignKey(Coach,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школи'


class Group(models.Model):
    name = models.CharField('Імя', max_length=20)
    school = models.ForeignKey(School,
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True)
    coach = models.ForeignKey(Coach,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True)

    def __str__(self):

        if self.school:
            groupSchool = str(self.school) + ' - ' + str(self.name)
            return groupSchool
        else:
            print(self.school)
            return 'Не вибрано зал - ' + self.name
        # school = self.name self.school

    class Meta:
        verbose_name = 'Група'
        verbose_name_plural = 'Групи'


class Timetable(models.Model):
    day = models.CharField('День', max_length=15)
    timeStart = models.TimeField('Час початку')
    timeFinish = models.TimeField('Час завершення')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.day

    class Meta:
        verbose_name = 'Графік'
        verbose_name_plural = 'Графіки'


class Sportsman(models.Model):
    first_name = models.CharField('Імя', max_length=20)
    last_name = models.CharField('Прізвище', max_length=25)
    surname = models.CharField('По батькові', max_length=20, blank=True)
    dateBirth = models.DateField('Дата народження')
    telephone = models.IntegerField('Номер телефону')
    belt = models.SmallIntegerField('Рівень поясу',
                                    choices=gradation,
                                    default=0,
                                    null=True)
    is_active = models.BooleanField('Тренується?', default=True)
    coach = models.ForeignKey(Coach,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмени'