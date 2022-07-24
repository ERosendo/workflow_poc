from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.translation import pgettext_lazy

from core.models import BaseModel, SoftDeletionQuerySet


class UserManager(BaseUserManager):
    def __init__(self, *args, **kwargs):
        self.alive_only = kwargs.pop('alive_only', True)
        super(UserManager, self).__init__(*args, **kwargs)

    def create_user(
        self,
        email,
        password=None,
        first_name=None,
        last_name=None,
        is_staff=False,
        is_active=True,
        groups=None,
        **extra_fields
    ):
        'Creates a User with a given first_name, last_name, email and password'
        email = UserManager.normalize_email(email.lower())
        user = self.model(
            email=email, is_active=is_active,
            first_name=first_name, last_name=last_name,
            is_staff=is_staff, **extra_fields
        )
        if password:
            user.set_password(password)
        if groups:
            user.groups = groups
        user.save()
        return user

    def create_superuser(self, email, password=None, first_name=None, last_name=None, groups=None, **extra_fields):
        return self.create_user(email=email,
                                password=password,
                                first_name=first_name,
                                last_name=last_name,
                                groups=groups,
                                is_staff=True,
                                is_superuser=True,
                                **extra_fields)

    def get_queryset(self):
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        return self.get_queryset().hard_delete()


class User(AbstractBaseUser, BaseModel):
    email = models.EmailField(
        pgettext_lazy('User field', 'email'),
        unique=True
    )
    first_name = models.CharField(
        pgettext_lazy('User field', 'first name'),
        max_length=256, blank=True, null=True
    )
    last_name = models.CharField(
        pgettext_lazy('User field', 'last name'),
        max_length=256, blank=True, null=True
    )
    is_staff = models.BooleanField(
        pgettext_lazy('User field', 'staff status'),
        default=False
    )
    is_active = models.BooleanField(
        pgettext_lazy('User field', 'active'),
        default=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'telephone']

    objects = UserManager()

    class Meta:
        verbose_name = pgettext_lazy('User model', 'user')
        verbose_name_plural = pgettext_lazy('User model', 'users')
        db_table = 'user'
