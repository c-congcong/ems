from django.db import models


# Create your models here.

# 管理员表
class Admin(models.Model):
    name = models.CharField(max_length=30)
    z_name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    sex = models.BooleanField()

    class Meta:
        db_table = 'admin'


# 员工表
class User(models.Model):
    name = models.CharField(max_length=40)
    # sex = models.BooleanField()
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    pic = models.ImageField(upload_to='img')

    class Meta:
        db_table = 'user'
