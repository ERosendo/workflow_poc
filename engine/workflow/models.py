from django.db import models
from django.utils.translation import pgettext_lazy

from core.models import BaseModel
from user.models import User
# Create your models here.

class Workflow(BaseModel):
    name = models.CharField(pgettext_lazy('Workflow field', 'name'), max_length=256)
    admins = models.ManyToManyField(User, related_name='workflows')
    
    class Meta:
        verbose_name = pgettext_lazy('Workflow model', 'workflow')
        verbose_name_plural = pgettext_lazy('Workflow model', 'workflows')
        db_table = 'workflow'