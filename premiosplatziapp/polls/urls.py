from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    # Para las view es necesario indicar el atribudo que va a usar para buscar en la Generic Vie Ej: pk
    path("",views.IndexView.as_view(), name = "index"),
    # path("", views.index, name="index"),
    path("<int:pk>/detail",views.DetailView.as_view(), name = "detail"),
    # path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("<int:pk>/results/",views.ResultView.as_view(), name = "results"),
    # path("<int:question_id>/results/", views.results, name="results"),

]