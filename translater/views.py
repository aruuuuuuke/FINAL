# views.py
from rest_framework import generics
from .models import Lesson, Word, Test, TestQuestion
from .serializers import LessonSerializer, WordSerializer, TestSerializer, TestQuestionSerializer


class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class WordListCreateView(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class TestListCreateView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestQuestionListCreateView(generics.ListCreateAPIView):
    queryset = TestQuestion.objects.all()

    serializer_class = TestQuestionSerializer

class TestQuestionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestQuestion.objects.all()
    serializer_class = TestQuestionSerializer
