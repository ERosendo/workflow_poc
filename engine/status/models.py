from django.db import models
from django.utils.translation import pgettext_lazy

from core.models import BaseModel
from workflow.models import Workflow


class StatusType(BaseModel):
    name = models.CharField(pgettext_lazy(
        'Status type field', 'name'), max_length=256)

    class Meta:
        verbose_name = pgettext_lazy('Status type model', 'status type')
        verbose_name_plural = pgettext_lazy('Status type model', 'status types')
        db_table = 'status_type'

    def __str__(self) -> str:
        return self.name


class Status(BaseModel):
    type = models.ForeignKey(StatusType, related_name='status', on_delete=models.CASCADE)
    workflow = models.ManyToManyField(Workflow, related_name='status', through='StatusWorkflow')
    name = models.CharField(pgettext_lazy('Status field', 'name'), max_length=256)
    description = models.CharField(pgettext_lazy('Status field', 'description'), max_length=256)

    class Meta:
        verbose_name = pgettext_lazy('Status model', 'status')
        verbose_name_plural = pgettext_lazy('Status model', 'statuses')
        db_table = 'status'

    def __str__(self) -> str:
        return self.name
    

class StatusWorkflow(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    workflow = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    position =  models.JSONField(default=dict())
    class Meta:
        db_table = 'status_workflow'