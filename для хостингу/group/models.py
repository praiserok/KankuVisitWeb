from django.db import models
from django.urls import reverse
from coach.models import Coach
from dodjo.models import School
from slugify import slugify
import random


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
