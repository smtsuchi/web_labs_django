from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='api-index'),
    path('courses/', views.getCourses, name='api-courses'),
    path('courses/<str:course_url>/', views.getCourse, name='api-course'),
    path('sections/<int:course_id>/', views.getSections, name='api-sections'),
    path('sections/<str:section_url>/', views.getSection, name='api-section'),
    path('lessons/<int:section_id>/', views.getLessons, name='api-lessons'),
    path('lessons/string/<str:section_url>/', views.getLessonsFromSectionURL, name='api-lessons-from-section-url'),
    path('lessons/<str:lesson_url>/', views.getLesson, name='api-lesson'),


    path('api/login/', obtain_auth_token, name='api-login'),
    path('api/register/', views.registerUser, name='api-register'),
    path('api/get-completed-lessons/', views.getCompletedLessons, name='api-get-completed-lessons'),
    path('api/mark-lesson-complete/', views.markLessonComplete, name='api-mark-lesson-complete'),

    path('prework/ide/compile/', views.compile, name='api-pythonide'),
]
