#coding:utf8
from wsgiref.simple_server import make_server # wsgi 内置模块
from controller import index,article

# url字典
urls = {
    '/' : index,
    '/article' : article,
}
def run(env,start_response): # env 用户请求环境变量 #响应参数
    start_response('200 ok',[('Content-Type','text/html')]) # 设置响应状态吗 和 响应文档类型
    path = env['PATH_INFO']
    # if path == '/': # 路由系统
    #     return index()
    # elif path == '/article':
    #     return article()
    # else:
    #     return '404'
    if path in urls.keys(): # url升级版
        fuc = urls[path]
        return fuc()
    else:
        return '404'

if __name__ == '__main__':
    http_server = make_server('127.0.0.1',8000,run) # 创建一个http服务
    http_server.serve_forever() # 启动http服务