from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('django-admin/', admin.site.urls),

    path('', include('accounts.urls')),

    path('admin-panel/', include('admin_panel.urls')),

    path('teacher/', include('teacher.urls')),

    path('student/', include('student.urls')),

]