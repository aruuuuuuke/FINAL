from django.contrib import admin
from django.urls import path, include

from translater.views import LessonAPView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/lessonlist/', LessonAPView.as_view()),
    path('api/v2/auth/', include('users.urls')),
]
