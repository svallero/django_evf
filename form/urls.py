from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf.urls import *
from form import views
from form.views import *

urlpatterns = patterns('',
   url(r'^$', login_required(views.CreateFarmView.as_view()), name='create_farm'),
   url(r'^(?P<pk>\d+)/$', login_required(views.DisplayFarmView.as_view()), name='display_farm'),
   url(r'^list$', login_required(views.ListFarmView.as_view()), name='list_farm'),
   url(r'^(?P<pk>\d+)/inst$', login_required(instantiate_view),name='instantiate_farm'),
   url(r'^(?P<pk>\d+)/del$', login_required(views.DeleteFarmView.as_view()),name='delete_farm'),
   url(r'^dashboard$', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
   )
