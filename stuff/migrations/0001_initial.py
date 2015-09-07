# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('date_given', models.DateTimeField()),
                ('was_taken', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=24)),
                ('date_joined', models.DateTimeField()),
                ('f_name', models.CharField(max_length=16)),
                ('l_name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=64)),
                ('is_active', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='thing',
            name='giver',
            field=models.ForeignKey(to='stuff.User'),
            preserve_default=True,
        ),
    ]
