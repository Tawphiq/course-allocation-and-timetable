# course_allocation/serializers.py

from rest_framework import serializers
from .models import Course, Department, Lecturer, Level, ClassGroup, LectureHall, Timetable

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'

class ClassGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = '__all__'

class LectureHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureHall
        fields = '__all__'

class TimetableSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    level = LevelSerializer()
    course = CourseSerializer()
    lecturer = LecturerSerializer()
    class_group = ClassGroupSerializer()
    lecture_hall = LectureHallSerializer()
    class Meta:
        """department = serializers.HyperlinkedRelatedField(many=True, view_name='department-detail', read_only=True)
        course = serializers.HyperlinkedRelatedField(many=True, view_name='course-detail', read_only=True)
        level = serializers.HyperlinkedRelatedField(many=True, view_name='level-detail', read_only=True)
        class_group = serializers.HyperlinkedRelatedField(many=True, view_name='classgroup-detail', read_only=True)
        lecture_hall = serializers.HyperlinkedRelatedField(many=True, view_name='lecture-hall-detail', read_only=True)
        lecturer = serializers.HyperlinkedRelatedField(many=True, view_name='lecturer-detail', read_only=True)"""


        model = Timetable
        fields = '__all__' 


"""from rest_framework import serializers
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id', 'department', 'level_type')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'department', 'course_level', 'name' )

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ('id', 'department', 'name')

class ClassGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = ('group_name')

class LectureHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureHall
        fields = ('id', 'department', 'name')

class TimetableSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    level = LevelSerializer()
    course = CourseSerializer()
    lecturer = LecturerSerializer()
    class_group = ClassGroupSerializer()
    lecture_hall = LectureHallSerializer()

    class Meta:
        model = Timetable
        fields = ('id', 'department', 'level', 'course', 'lecturer', 'class_group', 'lecture_hall', 'day', 'time_start', 'time_end', 'session_type')"""



