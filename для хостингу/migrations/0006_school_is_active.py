# Generated by Django 2.2.12 on 2022-02-04 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220204_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Працює?'),
        ),
    ]
