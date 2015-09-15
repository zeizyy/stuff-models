# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_auto_20150913_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='thing',
            name='location',
            field=models.CharField(max_length=20, default=None),
            preserve_default=False,
        ),
    ]
