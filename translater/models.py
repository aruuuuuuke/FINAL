# models.py
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Word(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    original_word = models.CharField(max_length=50)
    translated_word = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.original_word} ({self.translated_word})"


class Test(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    # user = models.CharField(max_length=50)
    score = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.lesson


class TestQuestion(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    user_translation = models.CharField(max_length=50)
    is_correct = models.BooleanField(default=False)
