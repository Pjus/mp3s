# Generated by Django 3.2.8 on 2021-10-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20211020_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='question',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='quiz_title',
            field=models.CharField(default='', max_length=128, verbose_name='quiz_title'),
        ),
    ]
