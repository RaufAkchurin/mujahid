# Generated by Django 4.2.7 on 2023-12-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mujahid_app', '0013_alter_day_dont_watch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='dont_watch',
            field=models.BooleanField(verbose_name='Не смотрел харам'),
        ),
        migrations.AlterField(
            model_name='day',
            name='looked_down',
            field=models.BooleanField(verbose_name='Потуплял взор'),
        ),
        migrations.AlterField(
            model_name='day',
            name='tg',
            field=models.BooleanField(),
        ),
    ]
