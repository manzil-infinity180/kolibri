# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-30 00:09
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [("content", "0007_auto_20180212_1155")]

    operations = [
        migrations.AlterField(
            model_name="contentnode",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="contentnode",
            name="license_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
