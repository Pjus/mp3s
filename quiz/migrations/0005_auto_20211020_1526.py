# Generated by Django 3.2.8 on 2021-10-20 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20211020_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='quiz_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizcontents', verbose_name='quiz_title'),
        ),
        migrations.AlterField(
            model_name='quizcontents',
            name='quiz_title',
            field=models.CharField(max_length=128, unique=True, verbose_name='quiz_title'),
        ),
    ]
