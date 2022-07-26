# Generated by Django 4.0.6 on 2022-07-21 14:17

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0003_workflow_admins_delete_workflowadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('cascade_deleted', models.BooleanField(null=True)),
                ('name', models.CharField(max_length=256, verbose_name='name')),
            ],
            options={
                'verbose_name': 'status type',
                'verbose_name_plural': 'status types',
                'db_table': 'status_type',
            },
        ),
    ]
