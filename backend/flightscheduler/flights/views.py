from django.shortcuts import render
from django.http import HttpResponse

def index(requrest):
    return HttpResponse("<h1>Hello</h1>")