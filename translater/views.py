from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer


class LessonAPView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

