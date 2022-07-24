from django.urls import re_path, include

from django.urls import re_path
from .users import views as user_views
from .workflow import views as workflow_views
from .status import views as status_views
from .transitions import views as transition_views

urlpatterns = [
    re_path(r'^users/$', user_views.user_list),
    re_path(r'^users/(?P<user_pk>[0-9a-f-]+)/$', user_views.user_detail),
    
    re_path(r'^workflows/$', workflow_views.workflow_list),
    re_path(r'^workflows/(?P<workflow_pk>[0-9a-f-]+)/$', workflow_views.workflow_detail),
    re_path(r'^workflows/(?P<workflow_pk>[0-9a-f-]+)/status/$', workflow_views.worflow_status),
    re_path(r'^workflows/(?P<workflow_pk>[0-9a-f-]+)/transitions/$', workflow_views.worflow_transitions),
    re_path(r'^workflows/add_administrator/', workflow_views.workflow_admin),
    re_path(r'^workflows/add_status/$', workflow_views.workflow_status),
    
    re_path(r'^status_type/$', status_views.status_type_list),
    re_path(r'^status_workflow/(?P<status_workflow_id>[0-9a-f-]+)/$', status_views.status_workflow),
    re_path(r'^status/$', status_views.status_list),
    
    re_path(r'^transitions/$', transition_views.transition),
    re_path(r'^transitions/(?P<transition_pk>[0-9a-f-]+)/$', transition_views.transition_detail)
]