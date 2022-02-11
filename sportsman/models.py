from django.db import models
from django.urls import reverse
from belt.models import Belt
from coach.models import Coach
from group.models import Group
from slugify import slugify


class Sportsman(models.Model):
    first_name = models.CharField('Імя', max_length=20)
    surname = models.CharField('По батькові', max_length=20, blank=True)
    last_name = models.CharField('Прізвище', max_length=25)
    dateBirth = models.DateField('Дата народження')
    telephone = models.IntegerField('Номер телефону')
    belts = models.ForeignKey(Belt,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    coach = models.ForeignKey(Coach,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    group = models.ForeignKey(Group,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    is_active = models.BooleanField('Тренується?', default=True)
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')

    def __str__(self):
        return self.first_name + " " + self.last_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.last_name + '-' +
                            self.first_name + '-' + self.surname)
        super(Sportsman, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Спортсмен'
        verbose_name_plural = 'Спортсмени'
        ordering = ['-is_active', 'coach', 'last_name']

    def get_absolute_url(self):
        return reverse('sportsman')
        # reverse("sportsman-edit", kwargs={"pk": self.pk})
