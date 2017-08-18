from django.conf.urls import url

from bluecollarbi.blog import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
]
