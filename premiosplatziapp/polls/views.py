from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.views import generic

# Enlace para las generics views: https://ccbv.co.uk/

# def index(request):
#     latest_question_list = Question.objects.all()
#     context = {
#         "latest_question_list": latest_question_list
#     }
#     return render(request, "polls/index.html",context)

#Esta generic view muestra una lista definida en el contexto en el template indicado con la queryset que retorna
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
         # Voy a retornar las ultimas 5 preguntas de las más nueva a la más vieja gracias al (-) y al ([:5])
        return Question.objects.order_by("-pub_date")[:5]

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         "question": question
#     }
#     return render(request, "polls/detail.html", context)

# Muestra el detalle de una pregunta expecifica
class DetailView(generic.DetailView):
    #Por debajo busca una question por un id recibido
    model = Question
    #Por debajo usa render para indicar que template usar
    template_name = "polls/detail.html"


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     context = {
#         "question":  question
#     }

#     return render(request, "polls/results.html", context)

# Usa la clase DetailView para usar la question y retorna al template indicado
class ResultView(DetailView):
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "quest": question,
        "error_message": "No eligiste una respuesta"
    }

    try:
        # Gracias a la forma en que Django se comunica con el HTML apartir del atributo name 
        # se identifica el input y se optiene el valor en el atributo value 
        selected_choice = question.choice_set.get(pk=request.POST["choice"])   
        # Si encuentra algun error continua con el except
    except (KeyError, Choice.DoesNotExist,): 
        # En caso de que haya un error al buscar la choice se envia el contexto con el error message
        return render(request, "polls/detail.html", context)
        # Si se encuentra un choice continua con el else para agregar la votación
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Buena practica al trabajar con formularios, redirigir al usuario para evitar enviar la información dos veces
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))


