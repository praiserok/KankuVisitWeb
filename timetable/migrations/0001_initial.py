# Generated by Django 2.2.12 on 2022-02-11 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimetableDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дні тиждня',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeStart', models.TimeField(verbose_name='Час початку')),
                ('timeFinish', models.TimeField(verbose_name='Час завершення')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('days', models.ManyToManyField(blank=True, to='timetable.TimetableDays')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
            ],
            options={
                'verbose_name': 'Графік',
                'verbose_name_plural': 'Графіки',
            },
        ),
    ]
