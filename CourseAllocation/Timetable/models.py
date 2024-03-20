# course_allocation/models.py

from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Level(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.department.name} - Level {self.name}"

class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100)
    course_level = models.PositiveSmallIntegerField()

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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='class_groups')

    def __str__(self):
        if self.group_name:
            return f"{self.course.name} - {self.group_name}"
        else:
            return f"{self.course.name} - Group {self.class_group_id}"

class LectureHall(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='lecture_halls')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Timetable(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='timetables')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    lecture_hall = models.ForeignKey(LectureHall, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    time_start = models.TimeField()
    time_end = models.TimeField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.level} - {self.class_group} - {self.day} - {self.time_start} to {self.time_end}"
