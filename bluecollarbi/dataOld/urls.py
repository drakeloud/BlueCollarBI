from django.conf.urls import url
from bluecollarbi.data import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^submit', views.submit, name='submit'),
    url(r'^analysis', views.analysis, name='analysis'),
    url(r'^forms', views.forms, name='forms'),
    url(r'^UDOTPrecastReport', views.UDOTPrecastReport, name='UDOTPrecastReport'),
    url(r'^barrierPostPour', views.barrierPostPour, name='barrierPostPour'),
]
