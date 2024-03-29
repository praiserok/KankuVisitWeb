# Generated by Django 4.0.6 on 2022-08-04 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('belt', '0001_initial'),
        ('dodjo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sportsman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Імя')),
                ('surname', models.CharField(blank=True, max_length=20, verbose_name='По батькові')),
                ('last_name', models.CharField(max_length=25, verbose_name='Прізвище')),
                ('dateBirth', models.DateField(blank=True, null=True, verbose_name='Дата народження')),
                ('is_active', models.BooleanField(default=True, verbose_name='Тренується?')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('belts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='belt.belt')),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dodjo.group')),
            ],
            options={
                'verbose_name': 'Спортсмен',
                'verbose_name_plural': 'Спортсмени',
                'ordering': ['-is_active', 'coach', 'last_name'],
            },
        ),
    ]
