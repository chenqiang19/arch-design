from wsgiref.simple_server import make_server
from paste import deploy
import os

def main():
    confPath = 'configure.ini'
    appPath = os.path.abspath(confPath)
    appname = 'main'
    wsgi_app = deploy.loadapp('config:%s' %appPath, name=appname)

    server = make_server('localhost', 8000, wsgi_app)
    server.serve_forever()

if __name__ == '__main__':
    main()