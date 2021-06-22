from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    print("Hello")
    return HttpResponse('<h1>Oi {} de {} anos</h1>'.format(nome, idade))

def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse(soma)

def multiplicacao(request, n1, n2):
    mult = n1 * n2
    return HttpResponse(mult)

def divisao(request, n1, n2):
    divisao = n1 / n2
    return HttpResponse(divisao)

def subtracao(request, n1, n2):
    return HttpResponse(n1 - n2)

