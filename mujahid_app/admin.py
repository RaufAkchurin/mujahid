from django.contrib import admin
from django.contrib.admin import site

from mujahid_app.models import Day


class DayAdmin(admin.ModelAdmin):
    list_display = ("date", "quran", "salat", "soum", "apathy_w", "time_pc", "time_wash", "looked_down", "dont_watch", "tg", "weekend", "yout_t", "az_subh", "az_asr", "masjeed", "happy_l")


site.register(Day, DayAdmin)
