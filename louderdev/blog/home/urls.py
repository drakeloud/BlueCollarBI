from django.conf.urls import url

from bluecollarbi.home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^elements', views.elements, name='elements'),
    url(r'^web-development', views.webDevelopment, name='web-development'),
    url(r'^automation', views.automation, name='automation'),
    url(r'^cloud', views.cloud, name='cloud'),
    url(r'^cyber-security', views.cyberSecurity, name='cyber-security'),
    url(r'^data-visualization', views.dataVisualization, name='data-visualization'),
    url(r'^predictive-analytics', views.predictiveAnalytics, name='predictive-analytics'),
]
