from turtle import position
from rest_framework import serializers

from status.models import Status, StatusType, StatusWorkflow


class StatusTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatusType
        fields = ('id', 'name')

class StatusChartSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source='status.name')

    class Meta:
        model = StatusWorkflow
        fields = ('id', 'label', 'status_id','position')
        read_only_fields = ['label']


class StatusSerializer(serializers.ModelSerializer):
    disable = serializers.SerializerMethodField(read_only=True)
    type_id = serializers.UUIDField(required=True)
    type = StatusTypeSerializer(required=False)

    class Meta:
        model = Status
        fields = ('id', 'name', 'type_id', 'type', 'disable')
        read_only_fields = ['type']
        
    def get_disable(self, obj):
        workflow = self.context.get('workflow', None)
        if not workflow:
            return False
        
        if obj.workflow.contains(workflow):
            return True
        return False
