from django.contrib import admin
from django.contrib.admin import site

from mujahid_app.models import Day

site.register(Day)
