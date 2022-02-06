from django.db import models
from django.urls import reverse
from belt.models import Belt
from coach.models import Coach
from group.models import Group


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
        return reverse("sportsman-edit", kwargs={"sportsman_id": self.pk})
