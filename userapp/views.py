import random
import string

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from userapp.captcha.image import ImageCaptcha

# Create your views here.

# 调取注册界面
from userapp.models import Admin


def regist(requset):
    return render(requset, 'userapp/regist.html')


# 验证码


def getcaptcha(request):
    image = ImageCaptcha()
    # 随机码
    code = random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 5)
    # 将验证码存入session
    random_code = ''.join(code)
    # print(random_code)
    request.session['code'] = random_code
    # 将随机字符拼接成字符串作为验证码图片文本
    data = image.generate(random_code)
    # 写出图片
    return HttpResponse(data, 'image/png')


# 验证
def registlogic(request):
    code = request.session.get('code')
    rst = request.POST.get('name')
    # print(code, rst)
    if code.lower() == rst.lower():
        return HttpResponse('true')
    return HttpResponse('false')


def check_name(request):
    name = request.POST.get('name')
    print(name)

    if Admin.objects.filter(name=name):
        return HttpResponse(True)
    return HttpResponse(False)


# 注册逻辑函数
def regist_fun(request):
    name = ''
    pwd = ''
    sex = ''
    z_name = ''
    if request.method == 'GET':
        name = request.GET.get('username')
        pwd = request.GET.get('userpwd')
        z_name = request.GET.get('name')
        sex = request.GET.get('sex')
    elif request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('userpwd')
        z_name = request.POST.get('name')
        sex = request.POST.get('sex')
    # 判断是否注册成功
    # print(name,pwd)
    # try:
    #     with transaction.atomic():
    rst = Admin.objects.create(name=name, pwd=pwd, sex=sex, z_name=z_name)
    print(123)
    if rst:
        return redirect('userapp:login')
    # except:
    return HttpResponse('注册失败!')


# 登录界面
def login(request):
    # 获取登录信息  监听是否设置过cookie
    name = request.COOKIES.get('username')
    pwd = request.COOKIES.get('userpwd')
    rst = Admin.objects.filter(name=name, pwd=pwd)
    if rst:
        request.session['login'] = True
        return redirect('adminapp:sel')
    return render(request, 'userapp/login.html')


# 登录逻辑
def login1(request):
    # name = request.POST.get('name')
    # pwd = request.POST.get('pwd')
    # rem = request.POST.get('rem')
    name=''
    pwd=''
    rem=''
    if request.method == 'GET':
        name = request.GET.get("name")
        pwd = request.GET.get("pwd")
        rem = request.GET.get("rem")
    elif request.method == 'POST':
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        rem = request.POST.get("rem")
    print(name,pwd,rem)
    # 2.验证 查询数据库
    if Admin.objects.filter(name=name, pwd=pwd):
        request.session['login'] = True
        res = redirect('adminapp:sel')
        if rem:  # 7天按钮选中
            res.set_cookie('username', name, max_age=7 * 24 * 3600)
            res.set_cookie('userpwd', pwd, max_age=7 * 24 * 3600)
            print(123)
        return res
    return HttpResponse('f')


# --------------------------------------------
# 练习
def asd():
    return HttpResponse('asd')
