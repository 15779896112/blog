# 自定义应用
# from views import *
import re
from urls import  *

def application(environ,start_response):
    # print(environ)
    # 遍历字典
    # for key in environ:
    #     print(key,'-----',environ[key])
    # print(environ['PATH_INFO'])
    html = "<html><head><meta charset='utf-8'></head><body>你好</body></html>"

    # 路由，将用户的请求转化为对应的处理
    path = environ['PATH_INFO']
    path = path.strip('/')  # 去掉前后的斜线
    print(path)
    # 第一版路由
    # if  path == '/':  #首页
    #     return index(environ,start_response)
    # elif path == '/login': #登陆页面
    #     return login(environ,start_response)

    # 第二版路由
    for pattern,func in urlpatterns:
        print(pattern,func)
        if re.match(pattern,path,re.I):
            return func(environ,start_response)

    # 匹配不上走下面的代码
    # 响应头
    start_response('200 ok',[('Content-Type','text/html')])

    return [html.encode('utf-8')]    # 响应体