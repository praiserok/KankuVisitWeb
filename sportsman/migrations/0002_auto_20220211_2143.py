# Generated by Django 2.2.12 on 2022-02-11 21:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sportsman', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsman',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, max_length=255, populate_from=('first_name', 'last_name', 'surname'), unique=True, verbose_name='URL'),
        ),
    ]
