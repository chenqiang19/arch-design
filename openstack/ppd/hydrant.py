class Hydrant(object):
    def __init__(self, in_arg):
        self.in_arg = in_arg
 
    def __call__(self, environ, start_response):
        print ('Hydrant class')
        start_response('200 ok', [('Content Type', 'text/plain')])
        return ['Hydrant'.encode("utf-8")]
 
def app_factory(global_config, in_arg):
    print(global_config)
    return Hydrant(in_arg)