from django.db import models
from django.urls import reverse
from coach.models import Coach


class School(models.Model):
    name = models.CharField('Назва', max_length=35)
    city = models.CharField('Місто', max_length=20)
    adress = models.CharField('Вулиця', max_length=35)
    coach = models.ForeignKey(Coach,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    is_active = models.BooleanField('Працює?', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школи'

    def get_absolute_url(self):
        return reverse('school')
