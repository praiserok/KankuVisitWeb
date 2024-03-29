# Generated by Django 4.0.6 on 2022-08-03 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Назва')),
                ('city', models.CharField(max_length=20, verbose_name='Місто')),
                ('adress', models.CharField(max_length=35, verbose_name='Вулиця')),
                ('is_active', models.BooleanField(default=True, verbose_name='Працює?')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('coach', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школи',
            },
        ),
    ]
