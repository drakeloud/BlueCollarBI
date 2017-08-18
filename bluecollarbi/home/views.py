from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string


def home(request):
    return render(request, 'home/index.html')

def services(request):
    return render(request, 'home/services.html')

def elements(request):
    return render(request, 'home/elements.html')

def webDevelopment(request):
    return render(request, 'home/web-development.html')

def automation(request):
    return render(request, 'home/automation.html')

def cloud(request):
    return render(request, 'home/cloud.html')

def cyberSecurity(request):
    return render(request, 'home/cyber-security.html')

def dataVisualization(request):
    return render(request, 'home/data-visualization.html')

def predictiveAnalytics(request):
    return render(request, 'home/predictive-analytics.html')
