from django.db import models
from django.db.models.fields import CharField
from edu.choices import *

# Create your models here.

class Quiz(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=128)
    quiz_title = models.CharField(max_length=128, unique=True, null=False, verbose_name="Question")
    question = models.CharField(max_length=200,null=True)
    answer1 = CharField(max_length=128, verbose_name="answer1")
    answer2 = CharField(max_length=128, verbose_name="answer2")
    answer3 = CharField(max_length=128, verbose_name="answer3")
    answer4 = CharField(max_length=128, verbose_name="answer4")
    answer5 = CharField(max_length=128, verbose_name="answer5")
    correct_answer = CharField(max_length=128, verbose_name="correct_answer")
