from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.cache import cache_page

# @cache_page(100,key_prefix='py2002')
from userapp.models import User


def query(request):
    # 查询 model数据 回传到html文件
    users = User.objects.all()
    return render(request, 'redisapp/query.html', {'users': users})


def change_age(request):
    rst = request.GET.get('age')
    user = User.objects.get(pk=1)
    user.age = rst
    user.save()
    # 手动清除缓存
    # 方式一：
    # caches = cache.keys('*py2002*')
    # for c in caches:
    #     cache.delete(c)
    # 方式二
    # caches = cache.keys('*py2002*')
    # cache.delete_many(caches)
    # 方式三：
    # cache.delete_pattern('*py2002*')
    # 方式四:
    # cache.clear()
    return HttpResponse('修改成功')


def set_session(request):
    request.session['python2002'] = True
    return HttpResponse('设置session')
