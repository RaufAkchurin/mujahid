# Generated by Django 4.2.7 on 2023-12-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mujahid_app', '0011_remove_day_problem_day_dont_watch_day_dua_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='dont_watch',
            field=models.BooleanField(default=False, verbose_name='Не смотрел харам'),
        ),
        migrations.AlterField(
            model_name='day',
            name='looked_down',
            field=models.BooleanField(default=False, verbose_name='Потуплял взор'),
        ),
    ]