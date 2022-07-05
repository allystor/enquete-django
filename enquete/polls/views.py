from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request,question_id):
    return HttpResponse(f"Esta é a questão {question_id}.")

def results(request,question_id):
    response = HttpResponse(f"Este é o resultado da questão {question_id}.")
    return response

def vote(request,question_id):
    return HttpResponse(f"Você votou na questão {question_id}.")