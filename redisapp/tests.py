# python连接redis
# from redis import Redis
#
# red = Redis(host='192.168.8.136',port=7000)
# print(red)

# 操作数据
# 存储键值对 name
# red.set('names','lileiabc')
# print(red.get('names').decode('utf-8')) # bytes

# 存储 列表
# red.rpush('list2',10,20,30)
# red.rpush('list3','马鹤群','杨洪举','静静')
# print(red.lrange('list2',0,-1))

# 数据类型： 字符串 列表 集合 有序集合 hash 命令符
# python redis实例对象 都有同名方法


# model数据存储
# from redisapp.models import User
# User.objects.create(name='lilei',age=18,birth='2000-1-1',salary=1000)
# User.objects.create(name='hanmeimei',age=19,birth='2001-1-1',salary=2000)
# User.objects.create(name='lintao',age=20,birth='2002-1-1',salary=3000)
# User.objects.create(name='lucy',age=21,birth='2003-1-1',salary=4000)
# User.objects.create(name='kata',age=22,birth='2004-1-1',salary=5000)


'''
把django下 model对象 进行 redis数据库存储
搭建django运行环境
'''
# import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "py_redis.settings")
# django.setup()

# from redis import Redis
# red = Redis(host='192.168.8.136',port=7000)
# print(red)
#
# from redisapp.models import User
#
# users = User.objects.all()  # queryset 对象 5条数据-model对象
# red.lpush('users',list(users)) # 字符串 列表 集合 有序集合 hash

# 类型转换 string
# s = '' 拼接  拼接成长串
# for u in users:
#     u.name

# json序列化 类型转换
# import json
#
# def mydefault(u):
#     if isinstance(u,User):
#         return {
#             'id': u.id,
#             'name':u.name,
#             'age':u.age,
#             'birth':u.birth.strftime('%Y-%m-%d'),
#             'salary':str(u.salary)}
#
#
# json_str = json.dumps(list(users),default=mydefault)
# print(json_str)
#
# red.set('users',json_str)

# 反序列化

# import os,django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "py_redis.settings")
# django.setup()
#
# import json
# from redis import Redis
# from redisapp.models import User
# red = Redis(host='192.168.8.136',port=7000)
# print(red)

# 读取数据
# rst = red.get('users')
# print(rst.decode('utf-8')) # 普通字符串
# s = rst.decode('utf-8') # 字符串
# 读取数据 反序列化 生成 model对象
# User(name=)
# json dumps json串
# json json串 反序列化为 数据类型
# print(json.loads(s),type(json.loads(s)))
# def myhook(d):
#     # return User(id=d['id'],name=d['name'],age=d['age'],salary=d['salary'],birth=d['birth'])
#     return User(**d)
# rst_list = json.loads(s,object_hook=myhook) # 列表
# print(rst_list)
# []
# for i in rst_list:
#     print(i,type(i)) # dict字典
#     User(name=i['name'],age=,birth=,salary=)
# python连接 redis集群
# from rediscluster import RedisCluster
# clunodes = [
#     {'host':'192.168.8.136','port':7001},
#     {'host':'192.168.8.136','port':7002},
#     {'host':'192.168.8.136','port':7003},
#     {'host':'192.168.8.136','port':7004},
#     {'host':'192.168.8.136','port':7005},
#     {'host':'192.168.8.136','port':7006},
# ]
# redclutor = RedisCluster(startup_nodes=clunodes)
# print(redclutor)
# # redclutor.set('weight','70kg')
# print(redclutor.get('weight').decode('utf-8'))