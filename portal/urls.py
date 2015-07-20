from django.conf.urls import *
from portal.views import *
from django.conf.urls import *
from form import views

urlpatterns = patterns('',

    # Main web portal entrance.
    #(r'^$', portal_main_page),
    url(r'^$', login_required(views.ListFarmView.as_view()), name='list_farm'),

)