import os
import uuid

from django.core.paginator import Paginator
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# 删除
from userapp.models import User


def dels(request):
    try:
        with transaction.atomic():
            num = request.GET.get('id')
            pg = request.GET.get('pg')
            request.session['pg'] = pg
            User.objects.get(id=num).delete()
            return redirect('adminapp:sel')
    except:
        return HttpResponse('失败')


def sel(request):
    # rst = request.session.get('log')
    # if rst:
    num = request.GET.get('id')
    pg = request.session.get('pg')
    try:
        with transaction.atomic():
            if not num:
                num = 1
                if pg:
                    num = pg
            user = User.objects.all()
            pgnator = Paginator(user, per_page=3)
            pg1 = pgnator.page(num)
            return render(request, 'adminapp/emplist.html', {'user': pg1})
    except:
        return HttpResponse('失败')
    # else:
    #     return redirect('user_admin:login')


# 修改
def upd1(request):
    num = request.GET.get('id')
    pg = request.GET.get('pg')
    request.session['id'] = num
    request.session['pg'] = pg
    user = User.objects.filter(pk=num)
    return render(request, 'adminapp/updateEmp.html', {'k1': num,
                                                       "user": user})


def upd(request):

    num = request.GET.get('id')
    name = request.POST.get('username')
    age = request.POST.get('userage')
    salary = request.POST.get('usersalary')
    img = request.FILES.get('img')
    rst = str(uuid.uuid4())  # 16位
    # 图文文件后缀获取
    # 元组 2个元素  第一个元素: 除了后缀之外路径  第二个元素：后缀
    sprst = os.path.splitext(img.name)
    img.name = rst + sprst[1]
    try:
        with transaction.atomic():
            new_user = User.objects.get(id=num)

            new_user.name = name
            new_user.age = age
            new_user.salary = salary
            new_user.pic = img
            new_user.save()
            return redirect('adminapp:sel')
    except:
        return HttpResponse('失败')


def add1(request):
    return render(request, 'adminapp/addEmp.html')


# 增加
def add(request):
    name = request.POST.get('username')
    age = request.POST.get('userage')
    salary = request.POST.get('usersalary')
    img = request.FILES.get('img')
    rst = str(uuid.uuid4())  # 16位
    # 图文文件后缀获取
    # 元组 2个元素  第一个元素: 除了后缀之外路径  第二个元素：后缀
    sprst = os.path.splitext(img.name)
    img.name = rst + sprst[1]
    # 添加数据
    try:
        with transaction.atomic():
            User.objects.create(name=name, age=age, salary=salary, pic=img)
            return redirect('adminapp:sel')
    except:
        return HttpResponse('失败')

# 时间
# def time(request):
