# Generated by Django 2.2.7 on 2021-05-16 03:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='episode',
        ),
        migrations.AddField(
            model_name='episode',
            name='file',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='episode', to='episodes.File'),
            preserve_default=False,
        ),
    ]
