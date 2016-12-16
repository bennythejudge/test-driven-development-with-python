# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]