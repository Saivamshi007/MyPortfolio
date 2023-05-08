from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from mybio.models import ProjectTable,TableforMessage
import numpy as np
from .forms import MessageTable
from django.views.decorators.csrf import csrf_protect,csrf_exempt

def index(request):
    project=ProjectTable.objects.all()
    form=MessageTable()
    context={
        'form':form,
        "projects":project,
        "skills":[{"color":tuple(np.random.choice(range(256), size=3)),"skill":"Python"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"Django REST FrameWork"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"PySpark"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"Tableau"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"NLP"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"AI"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"ML"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"TensorFlow"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"Java"},
                  {"color":tuple(np.random.choice(range(256), size=3)),"skill":"JavaScript"},
                  
                  ]

        # 'skils':['color''Python','Django REST FrameWork','PySpark',
        #          'Tableau','NLP','AI','ML','Oracle','JavaScript','Java'],
        # 'colors':[tuple(np.random.choice(range(256), size=3)) for i in range(10)]
    } 
    template=loader.get_template('index.html')
    return HttpResponse(template.render(context))

@csrf_exempt
def backTmsg(request):

    if request.method=='POST':
        msg=TableforMessage(message=request.POST.get("message"))
        msg.save()
        return HttpResponseRedirect('/mybio/thank_you/')


def thank_you(request):
    con={}
    temple=loader.get_template('thank_you.html')
    return HttpResponse(temple.render())