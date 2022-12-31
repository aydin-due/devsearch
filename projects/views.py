from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

def projects(request):
    context = { 'message': 'si', 'num': 10, 'projects': projectsList }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = {}
    for p in projectsList:
        if p['id'] == pk:
            project = p
    return render(request, 'projects/project.html', { 'project': project })