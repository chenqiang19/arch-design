from paste import deploy
import eventlet
from eventlet import wsgi
import os

conf_path = 'paste.ini'
app_path = os.path.abspath(conf_path)

def start():
    print("start wsgi server")
    myapp = deploy.loadapp("config:%s" % app_path, name='main')
    wsgi.server(eventlet.listen(('127.0.0.1', 9999)), myapp)


wsgi_server = eventlet.spawn(start)
wsgi_server.wait()
