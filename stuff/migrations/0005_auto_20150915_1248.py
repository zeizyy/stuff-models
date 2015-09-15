# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0004_thing_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
