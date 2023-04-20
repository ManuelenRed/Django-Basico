from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
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

def results(request, question_id):
    return HttpResponse(f"{question_id}")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "quest": question,
        "error_message": "No eligiste una respuesta"
    }

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        pass
    except (KeyError, Choice.DoesNotExist,): 
        return render(request, "polls/detail.html", context)

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


