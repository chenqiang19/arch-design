from oslo_policy import _parser
from oslo_policy.policy import DocumentedRuleDefault, RuleDefault
from typing import List

class Rule:
    def __init__(
        self,
        name: str,
        check_str: str,
        description: str,
        basic_check_str: str = "",
    ) -> None:
        self.name = name
        self.check_str = check_str
        self.check = _parser.parse_rule(self.check_str)
        self.description = description or "No description"
        self.basic_check_str = basic_check_str or self.check_str
        self.basic_check = _parser.parse_rule(self.basic_check_str)

    def __str__(self) -> str:
        return f'"{self.name}": "{self.check_str}"'

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(name='{self.name}', check_str='{self.check_str}')"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Rule) and isinstance(self, Rule):
            return (self.name, self.check_str) == (other.name, other.check_str)
        return False

    def format_into_yaml(self) -> str:
        desc = f"# {self.description}\n"
        text = f"{desc}{str(self)}\n\n"

        return text

    @classmethod
    def from_oslo(cls, rule: RuleDefault):
        description = rule.description or ""
        description = description.replace("\n", "\n#")
        return cls(name=rule.name, check_str=rule.check_str, description=description)
