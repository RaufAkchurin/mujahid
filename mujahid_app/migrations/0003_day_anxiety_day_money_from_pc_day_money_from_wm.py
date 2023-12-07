# Generated by Django 4.2.7 on 2023-11-27 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mujahid_app', '0002_rename_work_time_day_work_time_pc_day_work_time_wash_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='anxiety',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='day',
            name='money_from_pc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='day',
            name='money_from_wm',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]