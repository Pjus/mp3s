# Generated by Django 3.2.8 on 2021-10-20 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('음주운전', '음주운전'), ('공무집행방해', '공무집행방해'), ('도주치사상(뺑소니)', '도주치사상(뺑소니)'), ('사기죄', '사기죄'), ('명예훼손', '명예훼손'), ('모욕죄', '모욕죄'), ('공연음란죄', '공연음란죄'), ('강제추행', '강제추행'), ('강간', '강간'), ('뇌물', '뇌물'), ('보이스피싱', '보이스피싱'), ('카촬', '카촬'), ('주거침입', '주거침입'), ('통매음', '통매음'), ('교통범죄(신호위반 등) (교통특례법)', '교통범죄(신호위반 등) (교통특례법)'), ('폭행, 상해 등 폭력범죄', '폭행, 상해 등 폭력범죄'), ('마약', '마약'), ('도박', '도박'), ('강도', '강도'), ('업무방해', '업무방해'), ('협박', '협박'), ('운전자폭행', '운전자폭행'), ('성매매', '성매매'), ('아청법', '아청법'), ('음주측정거부', '음주측정거부'), ('절도', '절도'), ('성범죄 전반', '성범죄 전반'), ('코로나방역수칙위반(감염병예방법)', '코로나방역수칙위반(감염병예방법)'), ('재물손괴', '재물손괴'), ('아동학대', '아동학대'), ('횡령, 배임', '횡령, 배임')], max_length=128)),
                ('quiz_title', models.CharField(max_length=128, unique=True, verbose_name='Question')),
                ('question', models.CharField(max_length=200, null=True)),
                ('answer1', models.CharField(max_length=128, verbose_name='answer1')),
                ('answer2', models.CharField(max_length=128, verbose_name='answer2')),
                ('answer3', models.CharField(max_length=128, verbose_name='answer3')),
                ('answer4', models.CharField(max_length=128, verbose_name='answer4')),
                ('answer5', models.CharField(max_length=128, verbose_name='answer5')),
                ('correct_answer', models.CharField(max_length=128, verbose_name='correct_answer')),
            ],
        ),
    ]
