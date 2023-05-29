from typing import Any


class Drinking:
    def __init__(self) -> None:
        pass

    def __call__(self, environ: Any, start_response: Any) -> Any:
        print("Drinking class")
        start_response('200 ok', [('Content-Type', 'text/plain')])
        return ['Drinking']

def app_factory(global_config):
    return Drinking()