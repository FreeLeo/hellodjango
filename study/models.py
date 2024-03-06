# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Person(models.Model):
    name = models.CharField(primary_key=True, max_length=10, verbose_name='名字')
    age = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'person'
        verbose_name = '人员'
        verbose_name_plural = '人员复数'


class TbDept(models.Model):
    dno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=10, verbose_name='部门名称')
    dloc = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'tb_dept'
        verbose_name = '部门'
        verbose_name_plural = '部门复数'
        