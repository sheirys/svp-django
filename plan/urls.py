from django.conf.urls import url

from plan.views.project import ProjectListView
from plan.views.project import ProjectFormUpdateView
from plan.views.project import ProjectFormCreateView
from plan.views.task import TaskListView
from plan.views.task import TaskFormUpdateView
from plan.views.task import TaskFormCreateView

urlpatterns = [
	url(r'^project/$', ProjectListView.as_view(), name='ProjectListView'),
	url(r'^project/(?P<pk>\d+)/edit/$', ProjectFormUpdateView.as_view(), name='ProjectFormUpdateView'),
	url(r'^project/add/', ProjectFormCreateView.as_view(), name='ProjectFormCreateView'),
	url(r'^task/$', TaskListView.as_view(), name='TaskListView'), 
	url(r'^task/(?P<pk>\d+)/edit/$', TaskFormUpdateView.as_view(), name='TaskFormUpdateView'),
	url(r'^task/add/', TaskFormCreateView.as_view(), name='TaskFormCreateView'),
]
