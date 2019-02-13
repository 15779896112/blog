# 自定义应用

def application(environ,start_response):
    # print(environ)
    # 遍历字典
    # for key in environ:
    #     print(key,'-----',environ[key])
    print(environ['PATH_INFO'])
    html = "<html><head><meta charset='utf-8'></head><body>你好</body></html>"

    # 路由，将用户的请求转化为对应的处理
    path = environ['PATH_INFO']
    if  path == '/':
        html = "<!doctype html><head><meta charset='utf-8'></head><body><h1>Hello world</h1></body></html>"
    elif path == '/login': #登陆页面
        html = """
        
        """
    # 响应头
    start_response('200 ok',[('Content-Type','text/html')])

    return [html.encode('utf-8')]    # 响应体