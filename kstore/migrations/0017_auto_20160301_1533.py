# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kstore', '0016_auto_20160215_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailcontact',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='mailcontact',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mailmessage',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='mailmessage',
            name='sender',
        ),
        migrations.AlterField(
            model_name='basicconfiguration',
            name='company_name',
            field=models.CharField(verbose_name='Nombre de la empresa', max_length=255),
        ),
        migrations.AlterField(
            model_name='basicconfiguration',
            name='theme',
            field=models.CharField(verbose_name='Theme', max_length=255, default='one'),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(to='kstore.Manufacturer', blank=True, verbose_name='Manufacturer', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(to='kstore.Supplier', blank=True, verbose_name='Supplier', null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=255),
        ),
        migrations.DeleteModel(
            name='MailContact',
        ),
        migrations.DeleteModel(
            name='MailMessage',
        ),
    ]
