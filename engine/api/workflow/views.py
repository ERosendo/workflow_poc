from api.status.serializers import StatusChartSerializer
from api.transitions.serializers import TransitionFlowSerializer
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from status.models import StatusWorkflow

from workflow.models import Workflow

from .serializers import (WorkflowAdminSerializer, WorkflowSerializer,
                          WorkflowStatusSerializer)


class WorkflowViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = WorkflowSerializer
    lookup_url_kwarg = 'workflow_pk'

    def list(self, request, *args, **kwargs):
        """
        Retrieve list of workflows from database.
        """
        return super(WorkflowViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve certain workflow from database.
        """
        return super(WorkflowViewSet, self).retrieve(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        Updates a workflow from database.
        """
        return super(WorkflowViewSet, self).partial_update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Creates a workflow.
        """
        return super(WorkflowViewSet, self).create(request, *args, **kwargs)
    
    @action(detail=False, methods=['GET'])
    def list_status(self, request, workflow_pk, *args, **kwargs):
        """
        List of Status related to Workflow
        """
        instance = get_object_or_404(Workflow, pk = workflow_pk)
        return Response(StatusChartSerializer(instance.statusworkflow_set, many= True).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['GET'])
    def list_transitions(self, request, workflow_pk, *args, **kwargs):
        """
        List of Status related to Workflow
        """
        instance = get_object_or_404(Workflow.objects.all(), pk = workflow_pk)
        return Response(TransitionFlowSerializer(instance.transitions, many= True).data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        qs = Workflow.objects.all()
        return qs


class WorkflowAdminViewset(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = WorkflowAdminSerializer

    def create(self, request, *args, **kwargs):
        instance = WorkflowAdminSerializer(data=request.data)
        if instance.is_valid():
            workflow = instance.save()
            return Response(WorkflowSerializer(workflow).data, status=status.HTTP_200_OK)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkflowStatusViewset(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet
):

    serializer_class = WorkflowStatusSerializer
    lookup_url_kwarg = 'workflow_pk'

    def create(self, request, *args, **kwargs):
        instance = WorkflowStatusSerializer(data=request.data)
        if instance.is_valid():
            workflow = instance.save()
            return Response(StatusChartSerializer(workflow).data, status=status.HTTP_200_OK)
        return Response(instance.errors, status=status.HTTP_400_BAD_REQUEST)

workflow_list = WorkflowViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

workflow_detail = WorkflowViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
})

worflow_status = WorkflowViewSet.as_view({
    'get': 'list_status',
})

worflow_transitions = WorkflowViewSet.as_view({
    'get': 'list_transitions',
})


workflow_admin = WorkflowAdminViewset.as_view({
    'post': 'create'
})

workflow_status = WorkflowStatusViewset.as_view({
    'post': 'create'
})
