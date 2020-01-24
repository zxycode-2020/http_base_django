# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app02', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 26, 7, 57, 35, 84000, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
