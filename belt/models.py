from django.db import models
from django.urls import reverse


class Belt(models.Model):

    name = models.CharField('Назва', max_length=100)
    fullname = models.CharField(
        'Повна назва', max_length=100)
    number = models.IntegerField('Цифра пояса')
    img = models.ImageField('Картинка', upload_to='belt/%Y/', blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Пояс'
        verbose_name_plural = 'Пояси'

    def get_absolute_url(self):
        return reverse('belt')
