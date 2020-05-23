import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Greeting

# Create your views here.
'''
def index(request):
    # return HttpResponse('Hello from Python!')
    #return render(request, "index.html")
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')
'''
def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

@login_required(login_url='/login/')
def signup(request):
    return render(request, 'registration/signup.html')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

@login_required(login_url='/login/')
def text(request):

    return render(request, "text.html")

@login_required(login_url='/login/')
def contents(request):

    return render(request, "contents.html")

@login_required(login_url='/login/')
def omilia1(request):

    return render(request, "omilia1.html")

@login_required(login_url='/login/')
def omilia2(request):

    return render(request, "omilia2.html")

@login_required(login_url='/login/')
def omilia3(request):

    return render(request, "omilia3.html")

@login_required(login_url='/login/')
def omilia4(request):

    return render(request, "omilia4.html")

@login_required(login_url='/login/')
def omilia5(request):
    return render(request, "omilia5.html")

@login_required(login_url='/login/')
def omilia6(request):
    return render(request, "omilia6.html")

@login_required(login_url='/login/')
def omilia7(request):
    return render(request, "omilia7.html")

@login_required(login_url='/login/')
def kyrhgmata(request):
    return render(request, "kyrhgmata.html")