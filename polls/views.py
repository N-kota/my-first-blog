
from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from .models import Question, Choice
from .forms import *

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = VoteForm(request.POST, question=question)
        if form.is_valid():
            form.save()
            return redirect('polls:results', question_id=question.id)
    else:
        form = VoteForm(question=question)
    context = {'question':question, 'form':form}
    return render(request, "polls/detail.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
# Create your views here.
