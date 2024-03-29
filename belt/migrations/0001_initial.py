# Generated by Django 4.0.6 on 2022-08-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('fullname', models.CharField(max_length=100, verbose_name='Повна назва')),
                ('number', models.IntegerField(verbose_name='Цифра пояса')),
                ('img', models.ImageField(blank=True, upload_to='belt/%Y/', verbose_name='Картинка')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Пояс',
                'verbose_name_plural': 'Пояси',
            },
        ),
    ]
