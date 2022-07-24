from rest_framework import serializers

from api.status.serializers import StatusSerializer
from api.users.serializers import UserSerializer

from workflow.models import Workflow
from status.models import Status, StatusWorkflow
from user.models import User


class WorkflowSerializer(serializers.ModelSerializer):
    status = StatusSerializer(many=True, required = False)
    admins = UserSerializer(many=True, required = False)
    
    class Meta:
        model = Workflow
        fields = ('id', 'name', 'admins','status')
        read_only_fields = ['admins', 'status']
        
        
class WorkflowAdminSerializer(serializers.Serializer):
    workflow_id = serializers.UUIDField()
    user_id = serializers.UUIDField()
    
    def create(self, validated_data):
        workflow_id = validated_data['workflow_id']
        user_id = validated_data['user_id']
        
        workflow = Workflow.objects.filter(pk=workflow_id).first()
        user = User.objects.filter(pk=user_id).first()
        
        workflow.admins.add(user)
        
        return workflow
  

class WorkflowStatusSerializer(serializers.Serializer):
    workflow_id = serializers.UUIDField()
    status_id = serializers.UUIDField()
    position = serializers.JSONField(required=False)
    
    def create(self, validated_data):
        workflow_id = validated_data['workflow_id']
        status_id = validated_data['status_id']
        position = validated_data.get('position', None)
        
        workflow = Workflow.objects.filter(pk=workflow_id).first()
        status = Status.objects.filter(pk=status_id).first()
        
        if position:
            status_workflow = StatusWorkflow.objects.create(status = status, workflow = workflow, position=position)
        else:
            status_workflow = StatusWorkflow.objects.create(status = status, workflow = workflow)

        return status_workflow