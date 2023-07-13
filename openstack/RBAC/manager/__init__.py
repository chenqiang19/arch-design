from importlib import import_module
from os import path
from pkgutil import iter_modules

LIST_RULES_FUNC_NAME = "list_rules"

def get_service_rules():
    service_rules = {}
    current_path = path.dirname(path.abspath(__file__))
    for m in iter_modules(path=[current_path]):
        module = import_module(f"{__package__}.{m.name}")
        service_rules[m.name] = getattr(module, LIST_RULES_FUNC_NAME, [])
    
    return service_rules