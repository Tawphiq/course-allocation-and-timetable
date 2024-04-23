# course_allocation/views.py
""" from rest_framework import generics
from .models import Course, Department, Lecturer, Level, ClassGroup, LectureHall, Timetable
from .serializers import CourseSerializer, DepartmentSerializer, LecturerSerializer, LevelSerializer, ClassGroupSerializer, LectureHallSerializer, TimetableSerializer

class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class LevelListCreateView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LecturerListCreateView(generics.ListCreateAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

class LecturerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

class ClassGroupListCreateView(generics.ListCreateAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer

class ClassGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer

class LectureHallListCreateView(generics.ListCreateAPIView):
    queryset = LectureHall.objects.all()
    serializer_class = LectureHallSerializer

class LectureHallDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LectureHall.objects.all()
    serializer_class = LectureHallSerializer

class TimetableListCreateView(generics.ListCreateAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

class TimetableDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer """


from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response
from .models import *


class DepartmentViewset(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def list(self, request):
        queryset = Department.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class LevelViewset(viewsets.ViewSet):
    parser_classes = [permissions.AllowAny]
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

    def list(self, request):
        queryset = Level.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CourseViewset(viewsets.ViewSet):
    parser_classes = [permissions.AllowAny]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request):
        queryset = Course.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class LecturerViewset(viewsets.ViewSet):
    parser_classes = [permissions.AllowAny]
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

    def list(self, request):
        queryset = Lecturer.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ClassGroupViewset(viewsets.ViewSet):
    parser_classes = [permissions.AllowAny]
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer

    def list(self, request):
        queryset = ClassGroup.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)



class LectureHallViewset(viewsets.ViewSet):
    parser_classes = [permissions.AllowAny]
    queryset = LectureHall.objects.all()
    serializer_class = LectureHallSerializer

    def list(self, request):
        queryset = LectureHall.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class TimetableViewset(viewsets.ViewSet):
    #parser_classes = [permissions.AllowAny]
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

    def list(self, request):
        queryset = Timetable.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        timetable = self.queryset.get(pk=pk)
        serializer = self.serializer_class(timetable)
        return Response(serializer.data)

    def update(self, request, pk=None):
        timetable = self.queryset.get(pk=pk)
        serializer = self.serializer_class(timetable,data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        timetable = self.queryset.get(pk=pk)
        timetable.delete()
        return Response(status=204)

