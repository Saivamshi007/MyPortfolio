from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from mybio.models import ProjectTable
import numpy as np

def index(request):
    project=ProjectTable.objects.all()
    context={
        "projects":project,
        "skills":[{"color":"blue","skill":"Java"},{"color":"red","skill":"Python"}]

        # 'skils':['color''Python','Django REST FrameWork','PySpark',
        #          'Tableau','NLP','AI','ML','Oracle','JavaScript','Java'],
        # 'colors':[tuple(np.random.choice(range(256), size=3)) for i in range(10)]
    } 
    template=loader.get_template('index.html')
    return HttpResponse(template.render(context))

def projects():
    project=ProjectTable.objects.all()
    context={
        "projects":project
    }
    template=loader.get_template('projects.html')

    return HttpResponse(template.render(context))