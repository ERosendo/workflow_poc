from rest_framework import serializers

from api.workflow.serializers import WorkflowSerializer
from api.status.serializers import StatusChartSerializer

from transition.models import Transition

class TransitionFlowSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source = 'current_status_id')
    target = serializers.CharField(source = 'next_status_id')
    
    class Meta:
        model = Transition
        fields = ('id', 'source', 'target')
        

class TransitionSerializer(serializers.ModelSerializer):
    workflow_id = serializers.UUIDField()
    current_status_id = serializers.IntegerField()
    next_status_id = serializers.IntegerField()
    
    current_status = StatusChartSerializer(required=False)
    next_status = StatusChartSerializer(required=False)

    class Meta:
        model = Transition
        fields = ('id', 'workflow_id', 'current_status_id', 'current_status', 'next_status_id', 'next_status')
        read_only_fields = ['current_status', 'next_status']
