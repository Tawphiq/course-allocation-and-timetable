# course_allocation/urls.py

""" from django.urls import path
from . import views

urlpatterns = [
    # Department URLs
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),

    # Level URLs
    path('levels/', views.LevelListCreateView.as_view(), name='level-list-create'),
    path('levels/<int:pk>/', views.LevelDetailView.as_view(), name='level-detail'),


    # Course URLs
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),

    # Lecturer URLs
    path('lecturers/', views.LecturerListCreateView.as_view(), name='lecturer-list-create'),
    path('lecturers/<int:pk>/', views.LecturerDetailView.as_view(), name='lecturer-detail'),

    # Class Group URLs
    path('classgroups/', views.ClassGroupListCreateView.as_view(), name='classgroup-list-create'),
    path('classgroups/<int:pk>/', views.ClassGroupDetailView.as_view(), name='classgroup-detail'),

    # Lecture Hall URLs
    path('lecturehalls/', views.LectureHallListCreateView.as_view(), name='lecturehall-list-create'),
    path('lecturehalls/<int:pk>/', views.LectureHallDetailView.as_view(), name='lecturehall-detail'),

    # Timetable URLs
    path('timetables/', views.TimetableListCreateView.as_view(), name='timetable-list-create'),
    path('timetables/<int:pk>/', views.TimetableDetailView.as_view(), name='timetable-detail'),
] """


from django.urls import path 
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('departments', DepartmentViewset, basename='department')
router.register('levels', LevelViewset, basename='levels')
router.register('courses', CourseViewset, basename='courses')
router.register('lecturers', LecturerViewset, basename='lecturers')
router.register('classgroups', ClassGroupViewset, basename='classgroups')
router.register('lecturehalls', LectureHallViewset, basename='lecturehalls')
router.register('timetables', TimetableViewset, basename='timetables')
urlpatterns = router.urls
