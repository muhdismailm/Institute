from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('admin-login/', views.admin_login, name='admin_login'),

    path('teacher-login/', views.teacher_login, name='teacher_login'),

    path('student-login/', views.student_login, name='student_login'),

    path('logout/', views.user_logout, name='logout'),

]