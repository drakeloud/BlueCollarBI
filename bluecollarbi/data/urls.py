from django.conf.urls import url

from bluecollarbi.home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about', views.about, name='about'),
    url(r'^elements', views.elements, name='elements'),
]
