from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("You're at the poll idx")

def detail(request, question_id):
    return HttpResponse("Question pk %s" % question_id)

def results(request, question_id):
    return HttpResponse("Question results %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Voting on question %s" % question_id)