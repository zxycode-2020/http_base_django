# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20170727_1032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name': '\u73ed\u7ea7', 'verbose_name_plural': '\u73ed\u7ea7'},
        ),
        migrations.AddField(
            model_name='student',
            name='cls',
            field=models.ForeignKey(default=1, to='app01.Class'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=10, verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.DecimalField(null=True, verbose_name=b'\xe6\x88\x90\xe7\xbb\xa9', max_digits=5, decimal_places=2, blank=True),
        ),
    ]
