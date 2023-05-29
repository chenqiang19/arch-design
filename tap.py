from typing import Any


class Tap:
    def __init__(self) -> None:
        pass

    
    def __call__(self, environ: Any, start_response: Any) -> Any:
        print("Tag class")
        start_response('200 ok', [('Content-Type', 'text/plain')])
        return ['Tag']


def app_factory(global_config):
    return Tap()