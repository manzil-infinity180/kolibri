# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-14 21:19
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("logger", "0004_tidy_progress_range")]

    operations = [
        migrations.AddField(
            model_name="attemptlog",
            name="error",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="examattemptlog",
            name="error",
            field=models.BooleanField(default=False),
        ),
    ]
