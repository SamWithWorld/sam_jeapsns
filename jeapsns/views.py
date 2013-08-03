#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render_to_response,redirect
from jeapsns.models import sns
import datetime,os

from django.template import Template,Context
from django.template import RequestContext
from jeapsns.forms import snsForm
from django.contrib.auth.forms import *

def register(request):
    form = UserCreationForm()
    if request.method=="GET":
        return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/helloform")

        return render_to_response('register.html',{'form':form},context_instance=RequestContext(request))

def index_temp(request,input_name):

    t = Template('My name is {{name}}')
    c = Context({"name":input_name})
    return HttpResponse(t.render(c))

def hello(request):
    return HttpResponse("Hello world")


def hello2(request):
    return HttpResponse("Hello world")

def hello_get(request):
    if 'q' in request.GET:
        message = request.GET['q']
    return HttpResponse('hello world %s' % message)

def hello_getid(request):
    if 'id' in request.GET:
        id = request.GET['id']
        id =int(id) 
	if id ==0:
	      l1 = sns.objects.all()
	else:
	      l1 = sns.objects.get(id=id)
	      l1=[l1] #l1 is just one element,use [], let it iterable

	      '''
	      or use: l1 = sns.objects.filter(id=id)
	      '''
	return render_to_response('index_temp_file.html',{'l1':l1})

    return HttpResponse('hello world')

def hello_post(request):
    print dir(request)
    if request.method=='POST':
        name=request.POST['name']
        con= request.POST['content']
        n=sns()
        n.name=name
        n.content=con
        n.save()
    l1=sns.objects.all()
    return render_to_response('hello_post.html',{'l1':l1},context_instance=RequestContext(request))

def hello_form(request):
    
    #增加用户验证功能
    if request.user.is_authenticated():
        return render_to_response("layout.html",{'name':request.user.username})
    return HttpResponseRedirect("/accounts/login")
    
    if request.method=='POST':
        print '$'*20,request.POST 
        a=sns() 
        for n in request.POST.keys():
            if hasattr(a,n):
                setattr(a,n,request.POST[n])
	a.save()		
        '''
        name=request.POST['name']
        con =request.POST['content']
        n.sns()
        n.name=name
        n.content=con
        n.save()
        '''
    f = snsForm()
    l1=sns.objects.all()
    return render_to_response('hello_form.html',{'l1':l1,'f':f},context_instance=RequestContext(request))

def hello_delete(request):
    print '-'*15,request.GET,'-'*15
    if 'id' in request.GET:
        n = sns.objects.get(id=int(request.GET['id']))
        n.delete()
    return redirect('/helloform')

def hello_edit(request):
    if request.method=='GET':
	if 'id' in request.GET:
            mb = sns.objects.get(id=int(request.GET['id']))
	    f  = snsForm({'name':mb.name,'content':mb.content})
	    return render_to_response('hello_edit.html',{'f':f},context_instance=RequestContext(request))
    
    if request.method=='POST':
        a = sns.objects.get(id = int(request.GET['id']))
        a.name= request.POST['name']
        a.content=request.POST['content']
        print '%'*39,a
        a.save()
        '''
        for n in request.POST.keys():
            if hasattr(a,n):
               setattr(a,n,request.POST[n]) 
        a.save()       
        f=snsForm()
        l1=sns.objects.all()
        '''

        return redirect('/helloform')
    

def current_time(request,p):
    s = datetime.datetime.now()
    if p=='y':#如果用户输入的参数是y，则输出年
        p=s.year
    elif p=='m':#如果用户输入的参数是m，则输出月份
        p=s.month
    elif p=='d':#如用户输入的参数是d，则输出天
        p=s.day
    s1 = '%s----%s' % (s,p)
    return HttpResponse(s1)
def system_info(request,p):
    if p=='c':#cwd 获得当前路径
        s1=os.getcwd()
    return HttpResponse(s1)

#Using Model file
'''
def index_temp_file(request,input_name):
    return render_to_response('index_temp_file.html',{'name':input_name})    
'''

def index_temp_file(request,id):
    id = int(id)
    if id ==0:
        l1 = sns.objects.all()
    else:
        l1 = sns.objects.get(id=id) 
        print '*'*20,type(l1),'*'*6
        l1=[l1] #l1 is just one element,use [], let it iterable
        '''
        or use: l1 = sns.objects.filter(id=id)
        '''
    return render_to_response('index_temp_file.html',{'l1':l1})    
