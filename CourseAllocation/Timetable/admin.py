from django.contrib import admin
from .models import Department, Level, Course, Lecturer, ClassGroup, LectureHall, Timetable


admin.site.register(Department)
admin.site.register(Level)
admin.site.register(Course)
admin.site.register(Lecturer)
admin.site.register(ClassGroup)
admin.site.register(LectureHall)
admin.site.register(Timetable)
