from django.contrib import admin
from .models import Test, Lesson, Word, TestQuestion

admin.site.register(TestQuestion)
admin.site.register(Lesson)
admin.site.register(Word)
admin.site.register(Test)