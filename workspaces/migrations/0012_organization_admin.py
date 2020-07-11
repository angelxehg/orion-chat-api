# Generated by Django 3.0.7 on 2020-07-10 14:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspaces', '0011_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
