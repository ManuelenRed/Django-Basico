from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.all()
    context = {
        "latest_question_list": latest_question_list
    }
    return render(request, "polls/index.html",context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question
    }
    return render(request, "polls/detail.html", context)

def vote(request, question_id):
    return HttpResponse(f"Pagina de votación de la pregunta {question_id}")