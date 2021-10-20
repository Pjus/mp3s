# Generated by Django 3.2.8 on 2021-10-20 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20211020_1510'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['quiz_title'], 'verbose_name': 'Quiz', 'verbose_name_plural': 'Quiz'},
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='question',
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_title',
            field=models.CharField(default='', max_length=128, verbose_name='title'),
        ),
    ]