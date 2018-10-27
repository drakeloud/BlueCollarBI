from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from bluecollarbi.authentication import views as bluecollarbi_auth_views
from bluecollarbi.core import views as core_views
from bluecollarbi.home import views as home_views

urlpatterns = [
    url(r'^$', home_views.home, name='home'),
    url(r'^home/', include('bluecollarbi.home.urls')),
    url(r'^data/', include('bluecollarbi.data.urls')),
    url(r'^login', auth_views.LoginView.as_view(template_name='core/cover.html'), name='login'),
    url(r'^logout', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    url(r'^signup', bluecollarbi_auth_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
