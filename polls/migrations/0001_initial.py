# Generated by Django 5.0.3 on 2024-03-06 08:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('intro', models.CharField(max_length=1000, verbose_name='介绍')),
                ('is_hot', models.BooleanField(verbose_name='是否热门')),
            ],
            options={
                'verbose_name': '学科',
                'verbose_name_plural': '学科',
                'db_table': 'tb_subject',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('tel', models.CharField(max_length=20, verbose_name='手机号')),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('last_visit', models.DateTimeField(null=True, verbose_name='最后登录时间')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'tb_user',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('sex', models.BooleanField(default=True, verbose_name='性别')),
                ('birth', models.DateField(verbose_name='出生日期')),
                ('intro', models.CharField(max_length=1000, verbose_name='个人介绍')),
                ('photo', models.ImageField(max_length=255, upload_to='', verbose_name='照片')),
                ('good_count', models.IntegerField(db_column='gcount', default=0, verbose_name='好评数')),
                ('bad_count', models.IntegerField(db_column='bcount', default=0, verbose_name='差评数')),
                ('subject', models.ForeignKey(db_column='sno', on_delete=django.db.models.deletion.DO_NOTHING, to='polls.subject', verbose_name='学科')),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
                'db_table': 'tb_teacher',
                'managed': True,
            },
        ),
    ]
