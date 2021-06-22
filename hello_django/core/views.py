from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    print("Hello")
    return HttpResponse('<h1>Oi {} de {} anos</h1>'.format(nome, idade))
