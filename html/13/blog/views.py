# 定义各种处理


# 首页
def index(environ,start_response):
    start_response('200 ok', [('Content-Type', 'text/html')])
    return [b"<!doctype html><head><meta charset='utf-8'></head><body><h1>Hello world</h1></body></html>"]

# 登录
def login(environ,start_reponse):
    try:
        with open('templates/login.html') as fp:
            data = fp.read()
        start_reponse('200 ok', [('Content-Type', 'text/html')])
        return [data.encode('utf-8')]
    except Exception as e:
        data = "File Not Found"
        start_reponse('404 Not Found', [('Content-Type', 'text/html')])
        return [data.encode('utf-8')]
