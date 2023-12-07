from django.db import models


class Day(models.Model):
                    #rest
    awoke = models.TimeField(null=True)
    sunnah_duration = models.IntegerField(blank=True, null=True)
    sleep = models.TimeField(blank=True, null=True)
    weekend = models.BooleanField(default=False)

                    #education
    education_time = models.IntegerField(blank=True, null=True)
    din_ed_time = models.IntegerField(blank=True, null=True)

                    #deen
    az_subh = models.BooleanField(blank=True)
    az_asr = models.BooleanField(blank=True)
    quran = models.IntegerField(blank=True, null=True)
    masjeed = models.IntegerField(blank=True, null=True)
    soum = models.BooleanField(default=False)
    salat = models.BooleanField(default=False)

                    #work
    apathy_w = models.BooleanField(default=False)  # apathy_to_work
    time_pc = models.IntegerField(blank=True, null=True)  # work_time_pc
    time_wash = models.IntegerField(blank=True, null=True)  # work_time_wash
    money_pc = models.IntegerField(blank=True, null=True)
    money_wm = models.IntegerField(blank=True, null=True)


                    #addictions
    looked_down = models.BooleanField(verbose_name="Пот.взор")
    dont_watch = models.BooleanField(verbose_name="Не см.")
    tg = models.BooleanField()
    yout_t = models.IntegerField(blank=True, null=True) #youtube
    tauba = models.BooleanField(default=False)
    dua = models.BooleanField(default=False)

                    #psihosomatics
    happy_l = models.IntegerField(choices=[(i, str(i)) for i in range(0, 101, 10)])
    difficult_work = models.IntegerField(choices=[(i, str(i)) for i in range(0, 101, 10)])
    anxiety = models.BooleanField()
    date = models.DateField()

                    #sport
    sport = models.BooleanField(default=False)



    def __str__(self):
        return f"work {self.time_pc}  n/  |  quran {self.quran}  |  ed {self.education_time}  |  {self.date} |  {self.happy_l}"