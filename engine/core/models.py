import uuid

from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class SoftDeletionQuerySet(QuerySet):
    def delete(self, cascade=None):
        if cascade:
            return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now(), cascade_deleted=cascade)
        return super(SoftDeletionQuerySet, self).update(deleted_at=timezone.now())

    def restore(self, *args, **kwargs):
        return super(SoftDeletionQuerySet, self).update(deleted_at=None, cascade_deleted=None, **kwargs)

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at=None)

    def dead(self):
        return self.exclude(deleted_at=None)


class SoftDeletionManager(models.Manager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True, editable=False)
    cascade_deleted = models.BooleanField(null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True

    def delete(self, cascade=None):
        self.deleted_at = timezone.now()
        if cascade:
            self.cascade_deleted = True
        self.save()

    def restore(self):
        self.deleted_at = None
        self.cascade_deleted = None
        self.save()
