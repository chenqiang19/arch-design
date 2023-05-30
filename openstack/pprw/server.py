#coding=utf-8
import eventlet
from eventlet import wsgi
import routes.middleware
import webob.dec
import webob.exc
import functools
from resource_warpper import Resource


def action(name):
    """Mark a function as an action.

    The given name will be taken as the action key in the body.

    This is also overloaded to allow extensions to provide
    non-extending definitions of create and delete operations.
    """

    def decorator(func):
        func.wsgi_action = name
        return func
    return decorator


# 定义两个请求处理类Application1和Application2
class Application1(object):
    #def __call__(self, env, start_response):
    #    req = Request(env)
    #    response = Response(body="Welcome to wsgi, I'm in Application1.", content_type='text/plain')
    #    return response(env, start_response)
    def show(self, req):
        return {'msg': "Welcome to wsgi, I'm in Application1."}
        

class Application2(object):
    #def __call__(self, env, start_response):
    #    req = Request(env)
    #    response = Response(body="Welcome to wsgi, I'm in Application2.", content_type='text/plain')
    #    return response(env, start_response)
    def show(self, req):
        return {'msg': "Welcome to wsgi, I'm in Application2."}

def _create_controller(main_controller, action_controller_list):
    """This is a helper method to create controller with a
    list of action controller.
    """

    controller = Resource(main_controller())
    for ctl in action_controller_list:
        controller.register_actions(ctl())
    return controller

controller1 = functools.partial(
    _create_controller, Application1, [])

controller2 = functools.partial(
    _create_controller, Application2, [])

ROUTE_LIST = (
    ('/test1', {
        'GET': [controller1, 'show']
    }),
    ('/test2', {
        'GET': [controller2, 'show']
    }),
)

class Router(object):
    def __init__(self):
        self._mapper = routes.Mapper()                      # _mapper是空的
        #self._mapper.connect('/test1',                      # 给_mappper插入数据，建立url与controller的映射关系
        #                     controller=Application1(),
        #                     action='index',
        #                     conditions={'method': {'GET'}})
        #self._mapper.connect('/test2',                      # 给_mappper插入数据
        #                     controller=Application2(),
        #                     action='index',
        #                     conditions={'method': {'GET'}})
                             
        for path, methods in ROUTE_LIST:

            for method, controller_info in methods.items():
                controller = controller_info[0]()
                action = controller_info[1]
                self._mapper.connect(
                                path,
                                controller=controller,
                                action=action,
                                conditions={'method': {method}}
                            )
                #self.map.create_route(path, method, controller, action)

        self._router = routes.middleware.RoutesMiddleware(self._dispatch, self._mapper)  # 初始化，调用_dispatch方法取controller

    @webob.dec.wsgify
    def __call__(self, req):
        return self._router  # 调用

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            print("match is empty")
            return webob.exc.HTTPNotFound()
        return match['controller']  # return执行Application

def app_factory(global_config, **local_config):
    return Router()

def start():
    print("start wsgi server")
    myapp = Router()
    wsgi.server(eventlet.listen(('127.0.0.1', 9999)), myapp)

if __name__ == '__main__':
    wsgi_server = eventlet.spawn(start)
    wsgi_server.wait()
