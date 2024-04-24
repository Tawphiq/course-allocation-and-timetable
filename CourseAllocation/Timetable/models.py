# course_allocation/models.py

from django.db import models
from django.db.models import Case, When, Value, IntegerField

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Level(models.Model):
    LEVEL_TYPES = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('400', '400'),
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    level_type = models.CharField(max_length=10, choices=LEVEL_TYPES, default='100')

    def __str__(self):
        return f"{self.department.name} - Level {self.level_type}"

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, null=True, default=None)
    course_level = models.ForeignKey(Level, null=True, default=None, on_delete=models.CASCADE)
    credit_hours = models.PositiveIntegerField(default=3)


    def __str__(self):
        return self.name

class Lecturer(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='Lecturers')
    name = models.CharField(max_length=100)
    credit_hours_per_semester = models.PositiveIntegerField(default=12)

    def __str__(self):
        return self.name

class ClassGroup(models.Model):
    class_group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.group_name:
            return self.group_name
        else:
            return self.class_group_id

class LectureHall(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='lecture_halls')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Timetable(models.Model):
    SESSION_TYPES = (
        ('Regular', 'Regular'),
        ('Evening', 'Evening'),
        ('Weekend', 'Weekend'),
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='timetables')
    course = models.ForeignKey(Course, null=True, default=None, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    lecture_hall = models.ForeignKey(LectureHall, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    time_start = models.TimeField()
    time_end = models.TimeField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    session_type = models.CharField(max_length=10, choices=SESSION_TYPES, default="Regular")

    class Meta:
        ordering = [
            Case(
                When(day='Monday', then=Value(1)),
                When(day='Tuesday', then=Value(2)),
                When(day='Wednesday', then=Value(3)),
                When(day='Thursday', then=Value(4)),
                When(day='Friday', then=Value(5)),
                When(day='Saturday', then=Value(6)),
                When(day='Sunday', then=Value(7)),
                default=Value(8),  # Default value for days not listed (shouldn't happen ideally)
                output_field=IntegerField()
            ),
            'session_type',
            'time_start',  # Add secondary sorting by time_start
            'time_end'   # Add tertiary sorting by time_end

        ]

    def __str__(self):
        return f"{self.session_type} - {self.level} - {self.class_group} - {self.day}"

