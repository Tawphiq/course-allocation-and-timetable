# course_allocation/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Department URLs
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),

    # Level URLs
    path('levels/', views.LevelListCreateView.as_view(), name='level-list-create'),

    # Course URLs
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroyView.as_view(), name='course-retrieve-update-destroy'),

    # Lecturer URLs
    path('lecturers/', views.LecturerListCreateView.as_view(), name='lecturer-list-create'),
    path('lecturers/<int:pk>/', views.LecturerRetrieveUpdateDestroyView.as_view(), name='lecturer-retrieve-update-destroy'),

    # Class Group URLs
    path('classgroups/', views.ClassGroupListCreateView.as_view(), name='classgroup-list-create'),
    path('classgroups/<int:pk>/', views.ClassGroupRetrieveUpdateDestroyView.as_view(), name='classgroup-retrieve-update-destroy'),

    # Lecture Hall URLs
    path('lecturehalls/', views.LectureHallListCreateView.as_view(), name='lecturehall-list-create'),
    path('lecturehalls/<int:pk>/', views.LectureHallRetrieveUpdateDestroyView.as_view(), name='lecturehall-retrieve-update-destroy'),

    # Timetable URLs
    path('timetables/', views.TimetableListCreateView.as_view(), name='timetable-list-create'),
    path('timetables/<int:pk>/', views.TimetableRetrieveUpdateDestroyView.as_view(), name='timetable-retrieve-update-destroy'),
]
