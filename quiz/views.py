from django.shortcuts import render, get_object_or_404,redirect
from .models import Question,Choice,UserAnswer

# Create your views here.
def quiz_view(request):
    questions = Question.objects.all()

    return render(request,'quiz_app/quiz.html',{'questions':questions})

def score_view(request):
    if request.method=='GET':
        score = int(request.GET.get("score", 0))
        total_questions = int(request.GET.get("total", 0))
        return render(request, 'quiz_app/quiz_result.html', {'score': score, 'total_questions': total_questions})
