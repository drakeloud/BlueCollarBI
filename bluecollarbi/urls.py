from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from bluecollarbi.activities import views as activities_views
from bluecollarbi.authentication import views as bluecollarbi_auth_views
from bluecollarbi.core import views as core_views
from bluecollarbi.home import views as home_views
from bluecollarbi.search import views as search_views
from bluecollarbi.blog import views as blog_views

urlpatterns = [
    url(r'^$', home_views.home, name='home'),
    url(r'^blog/', include('bluecollarbi.blog.urls')),
    url(r'^home/', include('bluecollarbi.home.urls')),
    # URL pattern for profile home page
    url(r'^profilehome', core_views.profilehome, name='profilehome'),
    url(r'^login', auth_views.login, {'template_name': 'core/cover.html'},
        name='login'),
    url(r'^logout', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', bluecollarbi_auth_views.signup, name='signup'),
    url(r'^settings/$', core_views.settings, name='settings'),
    url(r'^settings/picture/$', core_views.picture, name='picture'),
    url(r'^settings/upload_picture/$', core_views.upload_picture,
        name='upload_picture'),
    url(r'^settings/save_uploaded_picture/$', core_views.save_uploaded_picture,
        name='save_uploaded_picture'),
    url(r'^settings/password/$', core_views.password, name='password'),
    url(r'^network/$', core_views.network, name='network'),
    url(r'^feeds/', include('bluecollarbi.feeds.urls')),
    url(r'^questions/', include('bluecollarbi.questions.urls')),
    url(r'^articles/', include('bluecollarbi.articles.urls')),
    url(r'^messages/', include('bluecollarbi.messenger.urls')),
    url(r'^notifications/$', activities_views.notifications,
        name='notifications'),
    url(r'^notifications/last/$', activities_views.last_notifications,
        name='last_notifications'),
    url(r'^notifications/check/$', activities_views.check_notifications,
        name='check_notifications'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^i18n/', include('django.conf.urls.i18n', namespace='i18n')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
