# Generated by Django 4.2.7 on 2023-12-05 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mujahid_app', '0009_day_salat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='azkar_asr',
            new_name='az_asr',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='azkar_subh',
            new_name='az_subh',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='happy_level',
            new_name='happy_l',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='youtube_time',
            new_name='yout_t',
        ),
    ]
