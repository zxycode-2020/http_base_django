# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stumanage', '0005_student_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xb0\x8f\xe7\xbb\x84\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u5174\u8da3\u5c0f\u7ec4',
                'verbose_name_plural': '\u5174\u8da3\u5c0f\u7ec4',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ManyToManyField(to='stumanage.Group'),
        ),
    ]
