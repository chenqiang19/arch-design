from http.server import BaseHTTPRequestHandler
import json
from policy import ENFORCER

# target模拟GenericCheck中的认证匹配如tenant_id,user_id,project_id
target = {'result': 'this is a test'}

# user_context模拟token中解析出的roles列表信息
user_context = {'roles': ['admin']}

def do_check():
    result = [
        {"rule": rule, "allowed": ENFORCER.authorize(rule, target, user_context)}
        for rule in ENFORCER.rules
    ]
    return result

class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        data = do_check()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_POST(self):
        datas = self.rfile.read(int(self.headers['content-length']))

        print('headers', self.headers)
        print("do post:", self.path, self.client_address, datas)