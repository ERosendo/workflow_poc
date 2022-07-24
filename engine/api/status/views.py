from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from workflow.models import Workflow

from status.models import Status, StatusType, StatusWorkflow

from .serializers import (StatusChartSerializer, StatusSerializer,
                          StatusTypeSerializer)


class StatusTypeViewset(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = StatusTypeSerializer
    
    def list(self, request, *args, **kwargs):
        """
        Retrieve list of users from database.
        """
        return super(StatusTypeViewset, self).list(request, *args, **kwargs)
    
    def get_queryset(self):
        qs = StatusType.objects.all()
        return qs
    

class StatusViewset(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    
    serializer_class = StatusSerializer
    
    def list(self, request, *args, **kwargs):
        """
        Retrieve list of status from database.
        """
        workflow_id = self.request.query_params.get('workflow_id', None)
        workflow = None
        if workflow_id:
            workflow = Workflow.objects.filter(pk=workflow_id).first()
       
        status_list = self.get_queryset()
        output_serializer = StatusSerializer(status_list, many= True, context={'workflow': workflow})
        
        return Response(output_serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create status.
        """
        return super(StatusViewset, self).create(request, *args, **kwargs)
    
    def get_queryset(self):
        qs = Status.objects.all()
        return qs

class StatusWorkflowViewset(
    mixins.UpdateModelMixin,
    
    viewsets.GenericViewSet
):
    
    serializer_class = StatusChartSerializer
    lookup_url_kwarg = 'status_workflow_id'
    
    def partial_update(self, request, *args, **kwargs):
        """
        Updates a status workflow from database.
        """
        return super(StatusWorkflowViewset, self).partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
    
        status_workflow = self.get_object()
        status_workflow.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_queryset(self):
        qs = StatusWorkflow.objects.all()
        return qs
    
    
status_type_list = StatusTypeViewset.as_view({
    'get': 'list'
})
   
   
status_list = StatusViewset.as_view({
    'get': 'list',
    'post': 'create'
})

status_workflow = StatusWorkflowViewset.as_view({
    'patch': 'partial_update',
    'delete': 'destroy'
})
