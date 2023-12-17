# urls.py
from django.urls import path
from .views import (
    LessonListCreateView, LessonDetailView,
    WordListCreateView, WordDetailView,
    TestListCreateView, TestDetailView,
    TestQuestionListCreateView, TestQuestionDetailView
)

urlpatterns = [
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),

    path('words/', WordListCreateView.as_view(), name='word-list-create'),
    path('words/<int:pk>/', WordDetailView.as_view(), name='word-detail'),

    path('tests/', TestListCreateView.as_view(), name='test-list-create'),
    path('tests/<int:pk>/', TestDetailView.as_view(), name='test-detail'),

    path('test-questions/', TestQuestionListCreateView.as_view(), name='test-question-list-create'),
    path('test-questions/<int:pk>/', TestQuestionDetailView.as_view(), name='test-question-detail'),
]
