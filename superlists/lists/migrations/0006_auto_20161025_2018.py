# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20161025_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='list',
            field=models.IntegerField(default=0),
        ),
    ]
