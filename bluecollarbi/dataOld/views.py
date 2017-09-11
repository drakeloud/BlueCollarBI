from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string


def index(request):
    return render(request, 'data/index.html')

def analysis(request):
    return render(request, 'data/analysis.html')

def submit(request):
    return render(request, 'data/submit.html')

def forms(request):
    return render(request, 'data/forms.html')

def UDOTPrecastReport(request):
    return render(request, 'data/UDOTPrecastReport.html')

def barrierPostPour(request):
    return render(request, 'data/barrierPostPour.html')
