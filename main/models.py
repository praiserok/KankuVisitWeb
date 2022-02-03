from django.db import models


class Task(models.Model):
    title = models.CharField('Назва', max_length=50)
    task = models.TextField('Опис')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завдання'
        verbose_name_plural = 'Завдання'
