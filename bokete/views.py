from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from .models import Image,Question, Choice
from .forms import ImageForm
from .forms import *

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'bokete/index.html', context)

def showall(request):
    images = Image.objects.all()
    context = {'images':images}
    return render(request, 'bokete/showall.html', context)
    
def detail(request, question_id):
    images = Image.objects.all()
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == 'POST':
        form = VoteForm(request.POST, question=question)
        if form.is_valid():
            form.save()
            return redirect('bokete:results', question_id=question.id)
    else:
        form = VoteForm(question=question)
    context = {'question':question, 'form':form,'images':images}

    return render(request, "bokete/detail.html", context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'bokete/results.html', {'question': question})    
# Create your views here.
