from django.conf import settings
from django.db import models

class Venue(models.Model):
    building = models.CharField(max_length=100)
    room = models.CharField(max_length=50)
    floor = models.CharField(max_length=20, blank=True)
    map_image = models.ImageField(upload_to="venue_maps/", blank=True, null=True)

    def __str__(self):
        return f"{self.building} - Room {self.room}"


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.code} on {self.date}"


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} enrolled in {self.course.code}"