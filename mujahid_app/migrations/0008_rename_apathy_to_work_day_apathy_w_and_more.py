# Generated by Django 4.2.7 on 2023-12-04 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mujahid_app', '0007_day_apathy_to_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='day',
            old_name='apathy_to_work',
            new_name='apathy_w',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='money_from_pc',
            new_name='money_pc',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='money_from_wm',
            new_name='money_wm',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='work_time_pc',
            new_name='time_pc',
        ),
        migrations.RenameField(
            model_name='day',
            old_name='work_time_wash',
            new_name='time_wash',
        ),
    ]
