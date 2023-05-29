from typing import Any


class Purifier:
    def __init__(self, app) -> None:
        self.app = app

    def __call__(self, environ: Any, start_response: Any) -> Any:
        print("Purifier class")
        return self.app(environ, start_response)
    
def filter_app_factory(app, global_config):
    return Purifier(app)