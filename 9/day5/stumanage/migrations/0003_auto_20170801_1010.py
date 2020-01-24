# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stumanage', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '\u7528\u6237\u4fe1\u606f', 'verbose_name_plural': '\u7528\u6237\u4fe1\u606f'},
        ),
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default=b'avatar/default.jpg', upload_to=b'avatar/', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
