# Generated by Django 2.2.12 on 2022-02-06 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('belt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Імя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Прізвище')),
                ('surname', models.CharField(blank=True, max_length=20, verbose_name='По батькові')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('password', models.CharField(blank=True, max_length=128, verbose_name='Пароль')),
                ('dateBirth', models.DateField(verbose_name='Дата народження')),
                ('telephone', models.IntegerField(verbose_name='Номер телефону')),
                ('telephone2', models.IntegerField(blank=True, null=True, verbose_name='Номер телефону 2')),
                ('information', models.TextField(verbose_name='Інформація про тренера')),
                ('photo', models.ImageField(blank=True, upload_to='coach/photo/%Y/%m/%d/', verbose_name='Фото')),
                ('is_active', models.BooleanField(default=True, verbose_name='Тренує?')),
                ('belts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='belt.Belt')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренери',
            },
        ),
    ]