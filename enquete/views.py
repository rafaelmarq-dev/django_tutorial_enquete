from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá, Caba! Você está no índice de enquetes.")
