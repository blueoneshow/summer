# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from models import Record
from django.template import RequestContext



def index(request):
        friends = ['tama', 'koma', 'pochi', 'ben', 'tora']
        return render_to_response('index.html', {'friends':friends})
    
def tama(request):
        return render_to_response('tama.html')
  
def koma(request):
         return render_to_response('koma.html') 

def add(request, seconds):
  record = Record(seconds=seconds)
  record.save()
  return redirect("/show")
  
def show(request):
  records = Record.objects.all().order_by("-id")
  return render_to_response('show.html',{'records':records}, context_instance=RequestContext(request))