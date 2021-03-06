# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_coursefeedbackdetail_stateindia_statewisedistrict_studentcourseregistration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidateregistration',
            old_name='c_preferred_trainig_state_ut',
            new_name='c_preferred_training_state_ut',
        ),
        migrations.AddField(
            model_name='studentcourseregistration',
            name='scr_has_given_feedback',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studentcourseregistration',
            name='scr_is_certified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='candidateregistration',
            name='c_alternate_contact_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='candidateregistration',
            name='c_contact_number',
            field=models.CharField(max_length=12),
        ),
    ]
