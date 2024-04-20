# course_allocation/views.py

from rest_framework import generics
from .models import Course, Department, Lecturer, Level, ClassGroup, LectureHall, Timetable
from .serializers import CourseSerializer, DepartmentSerializer, LecturerSerializer, LevelSerializer, ClassGroupSerializer, LectureHallSerializer, TimetableSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class LevelListCreateView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()  # Removed department filtering
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()  # Removed department filtering
    serializer_class = CourseSerializer

class LecturerListCreateView(generics.ListCreateAPIView):
    queryset = Lecturer.objects.all()  # Removed department filtering
    serializer_class = LecturerSerializer

class LecturerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()  # Removed department filtering
    serializer_class = LecturerSerializer

class ClassGroupListCreateView(generics.ListCreateAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer

class ClassGroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer

class LectureHallListCreateView(generics.ListCreateAPIView):
    queryset = LectureHall.objects.all()  # Removed department filtering
    serializer_class = LectureHallSerializer

class LectureHallRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LectureHall.objects.all()  # Removed department filtering
    serializer_class = LectureHallSerializer

class TimetableListCreateView(generics.ListCreateAPIView):
    queryset = Timetable.objects.all()  # Removed department filtering
    serializer_class = TimetableSerializer

class TimetableRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timetable.objects.all()  # Removed department filtering
    serializer_class = TimetableSerializer
