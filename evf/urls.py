from evf.views import *
from django.conf.urls import *
from django.contrib import admin

urlpatterns = patterns('',
    # admin
    url(r'^admin/', include(admin.site.urls)),
    # main page
    (r'^$', main_page),
    # login/logout
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    # web portal.
    (r'^portal/', include('portal.urls')),
    # serve static content.
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #    {'document_root': 'static'}),
    # create virtual farm
    url(r'^form/', include('form.urls', namespace="form")),
)
