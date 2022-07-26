# Generated by Django 4.0.6 on 2022-07-24 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0006_alter_status_type'),
        ('transition', '0002_alter_transition_workflow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transition',
            name='current_status',
        ),
        migrations.RemoveField(
            model_name='transition',
            name='next_status',
        ),
        migrations.AddField(
            model_name='transition',
            name='current_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transition', to='status.statusworkflow'),
        ),
        migrations.AddField(
            model_name='transition',
            name='next_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next_status', to='status.statusworkflow'),
        ),
    ]
