# Generated by Django 4.0.6 on 2022-08-02 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportsman', '0002_remove_sportsman_telephone_alter_sportsman_datebirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsman',
            name='dateBirth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата народження'),
        ),
    ]