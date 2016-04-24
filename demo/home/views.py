#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse

from .tasks import hello_world,sendEmail
 
def index(request):
    #hello_world.delay()
    #sendEmail.delay()
    #return HttpResponse(u"欢迎光临 自强学堂!")
    return render_to_response('index.html',locals())

def success(request):
    sendEmail.delay()
    return render_to_response('success.html',locals())
