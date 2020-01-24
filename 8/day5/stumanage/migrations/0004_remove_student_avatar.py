# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stumanage', '0003_auto_20170801_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='avatar',
        ),
    ]
