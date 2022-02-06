from unicodedata import name
from django.db import models
from django.urls import reverse


class Belt(models.Model):
    name = models.CharField('Назва', max_length=20)
    kyu = models.IntegerField('Кю')
    img = models.ImageField('Фото', upload_to='belt/%Y/', blank=True)

    def __str__(self):
        return self.kyu

    class Meta:
        verbose_name = 'Пояс'
        verbose_name_plural = 'Пояси'


class Coach(models.Model):

    first_name = models.CharField('Імя', max_length=20)
    last_name = models.CharField('Прізвище', max_length=25)
    surname = models.CharField('По батькові', max_length=20, blank=True)
    email = models.EmailField('Email', unique=True)
    password = models.CharField('Пароль', max_length=128, blank=True)
    dateBirth = models.DateField('Дата народження')
    telephone = models.IntegerField('Номер телефону')
    telephone2 = models.IntegerField('Номер телефону 2', blank=True, null=True)
    belts = models.ForeignKey(Belt,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    information = models.TextField('Інформація про тренера')
    photo = models.ImageField(
        'Фото', upload_to='coach/photo/%Y/%m/%d/', blank=True)
    is_active = models.BooleanField('Тренує?', default=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренери'

    def get_absolute_url(self):
        return reverse("coachedit", kwargs={"coach_id": self.pk})


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

    def get_absolute_url(self):
        return reverse("schooledit", kwargs={"school_id": self.pk})


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

    # def get_absolute_url(self):
    #     return reverse("group", kwargs={"groupid": self.pk})


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

    # def get_absolute_url(self):
    #     return reverse("timetable", kwargs={"timetableid": self.pk})


class Sportsman(models.Model):
    first_name = models.CharField('Імя', max_length=20)
    last_name = models.CharField('Прізвище', max_length=25)
    surname = models.CharField('По батькові', max_length=20, blank=True)
    dateBirth = models.DateField('Дата народження')
    telephone = models.IntegerField('Номер телефону')
    belts = models.ForeignKey(Belt,
                              on_delete=models.SET_NULL,
                              blank=True,
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

    def get_absolute_url(self):
        return reverse("sportsmanEdit", kwargs={"sportsman_id": self.pk})
