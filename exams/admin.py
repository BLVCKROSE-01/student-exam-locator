from django.contrib import admin
from .models import Venue, Course, Exam, Enrollment

admin.site.register(Venue)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Enrollment)