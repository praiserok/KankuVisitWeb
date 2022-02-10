from django.db import models
from django.urls import reverse
from coach.models import Coach
from school.models import School


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

    def get_absolute_url(self):
        return reverse('group')
