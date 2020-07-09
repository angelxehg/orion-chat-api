# Generated by Django 3.0.7 on 2020-07-09 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workspaces', '0009_workspace_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='workspace',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Organization',
        ),
        migrations.DeleteModel(
            name='Workspace',
        ),
    ]
