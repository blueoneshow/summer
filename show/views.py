# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
        friends = ['tama', 'koma', 'pochi', 'ben', 'tora']
        return render_to_response('index.html', {'friends':friends})
    
def tama(request):
        return render_to_response('tama.html')
  
def koma(request):
         return render_to_response('koma.html')     