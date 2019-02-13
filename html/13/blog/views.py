# 定义各种处理
from urllib.parse import parse_qs
from hashlib import sha1
from Manager import Manager

import jinja2

# 首页
# def index(environ,start_response):
#     start_response('200 ok', [('Content-Type', 'text/html')])
#     return [b"<!doctype html><head><meta charset='utf-8'></head><body><h1>Hello world</h1></body></html>"]
def index(request):
    request.start_response('200 ok', [('Content-Type', 'text/html')])
    return [b"<!doctype html><head><meta charset='utf-8'></head><body><h1>Hello world</h1></body></html>"]






# 登录
# def login(environ,start_reponse):
#     try:
#         with open('templates/login.html') as fp:
#             data = fp.read()
#         start_reponse('200 ok', [('Content-Type', 'text/html')])
#         return [data.encode('utf-8')]
#     except Exception as e:
#         data = "File Not Found"
#         start_reponse('404 Not Found', [('Content-Type', 'text/html')])
#         return [data.encode('utf-8')]
def login(request):
    try:
        with open('templates/login.html') as fp:
            data = fp.read()
        request.start_response('200 ok', [('Content-Type', 'text/html')])
        return [data.encode('utf-8')]
    except Exception as e:
        data = "File Not Found"
        request.start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [data.encode('utf-8')]


# 登录处理
# def doLogin(environ,start_response):
#     print(environ.get("QUERY_STRING"))
#     # 把参数字符串转化为字典
#     paras = parse_qs(environ.get('QUERY_STRING',''))
#     username = paras.get('username')
#     if username:
#         username = username[0]
#     password = paras.get('password')
#     if password:
#         password = password[0]
#         # 加密
#         password = sha1(password.encode('utf8')).hexdigest()
#     # print(username,password)
#
#     # 数据库操作
#     db = Manager('user')
#     result = db.where(name=username,password=password).select()
#     start_response('200 ok', [('Content-Type', 'text/html')])
#
#     # 如果查询成功
#     if result:
#         html=""
#         with open('templates/tip.html') as fp:
#             html = fp.read()
#         return [html.encode('utf-8')]
#     else:
#         return ["用户名或密码错误，请重新登陆".encode('utf-8')]

def doLogin(request):
    # 把参数字符串转化为字典
    paras = request.GET
    print(paras)
    username = paras.get('username')
    password = paras.get('password')
    password = sha1(password.encode('utf8')).hexdigest()
    # print(username,password)

    # 数据库操作
    db = Manager('user')
    result = db.where(name=username,password=password).select()
    request.start_response('200 ok', [('Content-Type', 'text/html')])

    # 如果查询成功
    if result:
        html=""
        with open('templates/tip.html') as fp:
            html = fp.read()
        return [html.encode('utf-8')]
    else:
        return ["用户名或密码错误，请重新登陆".encode('utf-8')]


# 学生列表
# def studentList(request):
#     html = """"
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>学生列表</title>
#     </head>
#     <body>
#     <table border="1" width="80%" align="center" cellspacing="0">
#         <caption>学生列表</caption>
#         <tr>
#             <th>学号</th>
#             <th>姓名</th>
#             <th>性別</th>
#             <th>生日</th>
#             <th>班級</th>
#         </tr>
#        {}
#     </table>
#     </body>
#     </html>
#     """
#     db = Manager('student')
#     data = db.values('sno,sname,ssex,sbirthday,sclass').select()
#     print(data)
#     from datetime import datetime
#     content = ""
#     for student in data:
#         content += "<tr><td>" + student.get('sno',' ') + "</td>"
#         content += "<td>" + student.get('sname',' ') + "</td>"
#         content += "<td>" + student.get('ssex',' ') + "</td>"
#         content += "<td>" + student.get('sbirthday',' ').strftime("%Y-%m-%d")  + "</td>"
#         if student.get('sclass',' '):
#             content += "<td>" + student.get('sclass',' ') + "</td></tr>"
#         else:
#             content += "<td>" + " " + "</td></tr>"
#
#     html = html.format(content)
#     # print(html)
#     request.start_response('200 ok', [('Content-Type', 'text/html')])
#     return [html.encode('utf-8')]

def studentList(request):
    db = Manager('student')
    data = db.values('sno,sname,ssex,sbirthday,sclass').select()
    print(data)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
    template = env.get_template('studentlist.html')
    print(template)
    request.start_response('200 ok', [('Content-Type', 'text/html')])
    return [template.render(students=data).encode('utf-8')]