# Generated by Django 4.0.6 on 2022-08-04 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dodjo', '0003_remove_timetable_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='costMoon',
            field=models.IntegerField(blank=True, null=True, verbose_name='Вартість місяця'),
        ),
        migrations.AddField(
            model_name='group',
            name='costTraining',
            field=models.IntegerField(blank=True, null=True, verbose_name='Вартість 1-го тренування'),
        ),
    ]