from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic

from .models import Question, Choice

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'test_app/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        l = Question.objects.order_by("-pub_date")[:5]
        return l

class DetailView(generic.DetailView):
    model = Question
    template_name = 'test_app/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'test_app/results.html'

def vote(request, q_id):
    q = get_object_or_404(Question, pk=q_id)
    try:
        selected = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "test_app/detail.html", {"question": q, "error_message": "You didn't select a choice."})
    else:
        selected.votes = F("votes") + 1
        selected.save()
        return HttpResponseRedirect(reverse("test_app:results", args=(q.id,)))