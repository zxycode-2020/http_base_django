# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stumanage', '0004_remove_student_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.ImageField(default=b'avatar/default.jpg', upload_to=b'avatar/', verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
