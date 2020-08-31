from django.db import models


class DjangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True)
    course_number = models.PositiveSmallIntegerField(default="", blank=True)
    instructor_name = models.CharField(max_length=60, default="", blank=True)
    duration = models.FloatField(default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

