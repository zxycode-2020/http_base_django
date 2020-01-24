# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20170727_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.DecimalField(null=True, verbose_name=b'\xe6\x88\x90\xe7\xbb\xa9', max_digits=5, decimal_places=2),
        ),
    ]
