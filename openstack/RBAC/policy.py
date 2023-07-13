from base import Enforcer
from manager import get_service_rules

ENFORCER = Enforcer()

def setup():
    service_rules = get_service_rules()
    all_api_rules = []
    
    for service, rules in service_rules.items():
        api_rules = []
        for rule in rules:
            api_rules.append(rule)
        all_api_rules.extend(api_rules)
    
    ENFORCER.register_rules(all_api_rules)