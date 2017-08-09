# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from question.models import Question
from django.shortcuts import render_to_response
from django.template import RequestContext
from question.forms import QuestionForm
from django.utils import timezone
from django.shortcuts import redirect

#def index(request):
        #questions = Question.objects.all()
        #response_string = "Questions <br/>"
        #response_string += '<br/>'.join(["id: %s, subject: %s" % (q.id, q.subject) for q in questions])
        #return HttpResponse(response_string)
      
#def question_detail(request, question_id):
        #question = Question.objects.get(pk=question_id)
        #return HttpResponse("%s?" % question.subject)
    
def index(request):
        questions = Question.objects.all()
        return render_to_response('question.html',{'questions': questions})

def question_detail(request, question_id):
        question = Question.objects.get(pk=question_id)
        return render_to_response('question_detail.html',{'question': question})
    
#def question_create(request):
        #form = QuestionForm()
        #return render_to_response('question_create.html',{'form': form}, context_instance=RequestContext(request))
    
def question_create(request):
        if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                        question = Question(subject=form.cleaned_data['subject'], publication_date=timezone.now())
                        question.save()
                        return redirect('/questions')
        else:
                form = QuestionForm()
        return render_to_response('question_create.html',{'form': form}, context_instance=RequestContext(request))
    
