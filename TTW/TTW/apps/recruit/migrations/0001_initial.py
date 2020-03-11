# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-01 12:02
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=20, null=True, verbose_name='城市名称')),
                ('ishot', models.SmallIntegerField(choices=[(0, '不是热门'), (1, '是热门')], default=1, null=True, verbose_name='是否热门')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
                'db_table': 'tb_city',
            },
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True, verbose_name='企业名称')),
                ('summary', models.CharField(default=None, max_length=1000, null=True, verbose_name='企业简介')),
                ('content', models.CharField(default=None, max_length=1000, null=True, verbose_name='企业详细信息')),
                ('city', models.CharField(default=None, max_length=100, null=True, verbose_name='企业所在城市')),
                ('address', models.CharField(default=None, max_length=100, null=True, verbose_name='企业地址')),
                ('labels', models.CharField(default=None, help_text='多个标签以空格隔开', max_length=100, null=True, verbose_name='标签列表')),
                ('coordinate', models.CharField(default=None, max_length=100, null=True, verbose_name='企业坐标')),
                ('logo', models.ImageField(default=None, null=True, upload_to='', verbose_name='Logo')),
                ('url', models.CharField(default=None, max_length=100, null=True, verbose_name='URL')),
                ('visits', models.BigIntegerField(default=0, null=True, verbose_name='浏览量')),
                ('users', models.ManyToManyField(related_name='enterpises', to=settings.AUTH_USER_MODEL, verbose_name='收藏者')),
            ],
            options={
                'verbose_name': '企业',
                'verbose_name_plural': '企业',
                'db_table': 'tb_enterprise',
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(default=None, max_length=100, null=True, verbose_name='职位名称')),
                ('salary', models.CharField(default=None, max_length=1000, null=True, verbose_name='薪资范围')),
                ('condition', models.CharField(default=None, max_length=100, null=True, verbose_name='经验要求')),
                ('education', models.CharField(default=None, max_length=100, null=True, verbose_name='学历要求')),
                ('type', models.CharField(default=None, max_length=10, null=True, verbose_name='任职方式')),
                ('city', models.CharField(default=None, max_length=100, null=True, verbose_name='办公所在城市')),
                ('address', models.CharField(default=None, max_length=100, null=True, verbose_name='办公地址')),
                ('state', models.SmallIntegerField(choices=[(0, '不可用'), (1, '可用')], default=1, null=True, verbose_name='状态')),
                ('labels', models.CharField(default=None, help_text='多个标签以空格隔开', max_length=100, null=True, verbose_name='职位标签')),
                ('detailcontent', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='职位描述')),
                ('detailrequire', ckeditor_uploader.fields.RichTextUploadingField(default='', verbose_name='职位要求')),
                ('visits', models.BigIntegerField(default=0, null=True, verbose_name='浏览量')),
                ('createtime', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建日期')),
                ('enterprise', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recruits', to='recruit.Enterprise', verbose_name='企业ID')),
                ('users', models.ManyToManyField(related_name='retruits', to=settings.AUTH_USER_MODEL, verbose_name='收藏者')),
            ],
            options={
                'verbose_name': '职位',
                'verbose_name_plural': '职位',
                'db_table': 'tb_recruit',
            },
        ),
    ]