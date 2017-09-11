from django.conf.urls import url
from bluecollarbi.data import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    
    url(r'^index', views.index, name='index'),

    # url(r'^form', views.form, name='form'),
    url(r'^.*\.html', views.gentella_html, name='gentella'),
    
]