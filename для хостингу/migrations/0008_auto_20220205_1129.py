# Generated by Django 2.2.12 on 2022-02-05 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20220204_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('name', models.CharField(max_length=20,
                                          verbose_name='Назва')),
                ('kyu', models.IntegerField(max_length=20, verbose_name='Кю')),
                ('img',
                 models.ImageField(blank=True,
                                   upload_to='belt/%Y/',
                                   verbose_name='Фото')),
            ],
        ),
        migrations.DeleteModel(name='Task', )
    ]
