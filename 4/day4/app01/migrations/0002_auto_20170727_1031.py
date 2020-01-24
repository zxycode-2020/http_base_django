# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u5b66\u751f', 'verbose_name_plural': '\u5b66\u751f'},
        ),
        migrations.AlterField(
            model_name='student',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\xb9\xb4\xe9\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.DecimalField(verbose_name=b'\xe6\x88\x90\xe7\xbb\xa9', max_digits=5, decimal_places=2),
        ),
    ]
