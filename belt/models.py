from django.db import models


class Belt(models.Model):
    name = models.CharField('Назва', max_length=20)
    kyu = models.IntegerField('Кю')
    img = models.ImageField('Фото', upload_to='belt/%Y/', blank=True)

    def __str__(self):
        return self.kyu

    class Meta:
        verbose_name = 'Пояс'
        verbose_name_plural = 'Пояси'
