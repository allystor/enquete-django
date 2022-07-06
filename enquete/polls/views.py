from django import http
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Questions
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-pub_date')[:5]


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'results.html'


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,"index.html", context)

def results(request,question_id):
    response = Questions(pk=question_id)
    return render(request, "results.html", {'polls:response': response})

def vote(request,question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request,"vote.html",{
            'question': question,
            'error_message': "Voce não selecionou nenhuma opcao",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))