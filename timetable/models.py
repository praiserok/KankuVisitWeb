from django.db import models
from django.urls import reverse
from group.models import Group


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
