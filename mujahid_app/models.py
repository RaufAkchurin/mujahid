from django.db import models


class Day(models.Model):
                    #rest
    awoke = models.TimeField(null=True)
    sunnah_duration = models.IntegerField(blank=True, null=True)
    sleep = models.TimeField(blank=True, null=True)

                    #education
    education_time = models.IntegerField(blank=True, null=True)
    din_ed_time = models.IntegerField(blank=True, null=True)

                    #deen
    azkar_subh = models.BooleanField(blank=True)
    azkar_asr = models.BooleanField(blank=True)
    quran_str = models.IntegerField(blank=True, null=True)
    masjeed = models.IntegerField(blank=True, null=True)

                    #work
    work_time_pc = models.IntegerField(blank=True, null=True)
    work_time_wash = models.IntegerField(blank=True, null=True)

                    #addictions
    problem = models.BooleanField()
    youtube_time = models.IntegerField(blank=True, null=True)

                    #psihosomatics
    happy_level = models.IntegerField(choices=[(i, str(i)) for i in range(0, 101, 10)])
    difficult_work = models.IntegerField(choices=[(i, str(i)) for i in range(0, 101, 10)])
    date = models.DateField()



    def __str__(self):
        return f"work {self.work_time_pc}  n/  |  quran {self.quran_str}  |  ed {self.education_time}  |  {self.date}"