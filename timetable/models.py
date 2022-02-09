from django.db import models
from django.urls import reverse
from group.models import Group
from django.utils.dateformat import DateFormat, TimeFormat

DAYS_OF_WEEK = [
    ('Понеділок', 'Понеділок'),
    ('Вівторок', 'Вівторок'),
    ('Середа', 'Середа'),
    ('Четвер', 'Четвер'),
    ('Пятниця', 'Пятниця'),
    ('Субота', 'Субота'),
    ('Неділя', 'Неділя'),
]


class Timetable(models.Model):

    days = models.CharField(max_length=15, choices=DAYS_OF_WEEK)
    timeStart = models.TimeField('Час початку')
    timeFinish = models.TimeField('Час завершення')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):

        print(str(self.days) + str(self.timeStart))
        formatted_time = TimeFormat(self.timeStart)
        formatted_time.format('h')
        return str(self.days) + ' - ' + str(formatted_time.format('H:i'))

    class Meta:
        verbose_name = 'Графік'
        verbose_name_plural = 'Графіки'

    def get_absolute_url(self):
        return reverse('timetable')
