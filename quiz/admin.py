from django.contrib import admin
from .models import Quiz, QuizContents

class Quizadmin(admin.ModelAdmin):
    list_display = ['category', 'quiz_title']

# Register your models here.
admin.site.register(QuizContents, Quizadmin)
admin.site.register(Quiz)