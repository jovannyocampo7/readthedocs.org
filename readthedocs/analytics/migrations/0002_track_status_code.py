# Generated by Django 3.2.12 on 2022-03-17 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("builds", "0041_track_task_id"),
        ("projects", "0087_use_booleanfield_null"),
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pageview",
            name="status",
            field=models.PositiveIntegerField(
                default=200, help_text="HTTP status code"
            ),
        ),
        migrations.AlterField(
            model_name="pageview",
            name="version",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="page_views",
                to="builds.version",
                verbose_name="Version",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="pageview",
            unique_together={("project", "version", "path", "date", "status")},
        ),
    ]
