from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('projects')

def project(request, pk):
    return HttpResponse(f'project {pk}')