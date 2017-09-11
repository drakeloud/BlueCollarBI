from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    context = {}
    template = loader.get_template('data/index.html')
    return HttpResponse(template.render(context, request))

def form(request):
    return render(request, 'data/form.html')

def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('data/' + load_template)
    return HttpResponse(template.render(context, request))

