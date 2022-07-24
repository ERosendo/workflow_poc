# Generated by Django 4.0.6 on 2022-07-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_options_alter_user_table'),
        ('workflow', '0002_workflowadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflow',
            name='admins',
            field=models.ManyToManyField(related_name='workflows', to='user.user'),
        ),
        migrations.DeleteModel(
            name='WorkflowAdmin',
        ),
    ]
