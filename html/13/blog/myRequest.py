# 封装请求类
from urllib.parse import parse_qs

class MyRequest:
    def __init__(self,environ,start_response):
        self.start_response = start_response
        self.environ = environ

        # 请求方法
        self.method = environ.get('REQUEST_METHOD','GET')
        # 请求路径
        self.path = environ.get('PATH_INFO','/')

        #get参数
        self.GET = self.get_parameters()

    # 获取get参数
    def get_parameters(self):
        queryString = self.environ.get('QUERY_STRING','')
        data = parse_qs(queryString)
        """
        {'username':['admin']}
        """
        for key in data:
            if len(data[key]) == 1:
                data[key] = data[key][0]
        return data