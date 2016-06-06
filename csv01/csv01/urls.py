from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'csv01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    #url(r'^index/', 'blog.views.index'),
    #url(r'^index1/', 'blog.views.index1'),
    #url(r'^index2/', 'blog.views.index2'),
)
