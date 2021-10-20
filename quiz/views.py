from django.shortcuts import render, get_object_or_404
from .models import QuizContents, Quiz
# Create your views here.
def index(request):
    contents = QuizContents
    quiz_list = contents.objects.order_by('id')
    contents = {
        'quiz_list' : quiz_list,
    }
    return render(request, 'quiz/index.html', contents)

def detail(request, pk):
    notice = get_object_or_404(Quiz, pk=pk)
    contents = {
        'notice' : notice,
    }
    return render(request, 'quiz/detail.html', contents)