from oslo_policy._checks import _check


class Enforcer:
    rules = {}
    
    def register_rules(self, rules):
        rule_map = {}
        for rule in rules:
            if rule.name in rule_map:
                raise ValueError("Duplicate policy rule.")
            
            rule_map[rule.name] = rule.basic_check
            
        self.rules = rule_map
        
    
    def authorize(self, rule, target, context):
        result = False
        do_check = self.rules.get(rule)
        if do_check is None:
            raise ValueError("Policy not registered")
        
        result = _check(
                        rule=do_check, 
                        target=target,
                        creds=context,
                        enforcer=self,
                        current_rule=rule,
                    )
        
        return result