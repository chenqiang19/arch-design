from typing import Any


class Shower:
    def __init__(self) -> None:
        pass
    
    def __call__(self, environ: Any, start_response: Any) -> Any:
        print("Shower class")
        start_response('200 ok', [('Content-Type', 'text/plain')])
        return ['Shower'.encode("utf-8")]

def app_factory(global_config):
    return Shower()