from django.db import models
from core.models import BaseModel

from workflow.models import Workflow
from status.models import StatusWorkflow


class Transition(BaseModel):
    workflow = models.ForeignKey(Workflow, related_name='transitions', on_delete=models.CASCADE)
    current_status = models.ForeignKey(StatusWorkflow, related_name='transition', on_delete=models.CASCADE)
    next_status = models.ForeignKey(StatusWorkflow, related_name='next_status', on_delete=models.CASCADE)

    class Meta:
        db_table = 'transition'
