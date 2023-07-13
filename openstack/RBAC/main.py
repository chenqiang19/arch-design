# 启动一个server
# setup policy
# policy注册
# policy认证

import http.server
import socketserver
import policy as policies_setup
import request

PORT = 8088

def init():
    policies_setup.setup()

def setup ():
    #SimpleHTTPRequestHandler会解析当前项目的目录结构返回给请求
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("localhost", PORT), request.Resquest) as httpd:
        httpd.serve_forever()


init()
setup()
