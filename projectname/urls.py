from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projectname.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^graph/$','application.views.Graph'),
    url(r'^graph2/$','application.views.Graph2'),
    url(r'^graph3/$','application.views.Graph3'),
    url(r'^graph4/$','application.views.Graph4'),
)
