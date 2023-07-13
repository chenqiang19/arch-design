from . import base

list_rules = (
    base.Rule(
        name="context_is_admin",
        check_str=("role:admin"),
        description="Rule for cloud admin access",
    ),
    base.Rule(
        name="owner",
        check_str=("tenant_id:%(tenant_id)s"),
        description="Rule for resource owner access",
    ),
    base.Rule(
        name="admin_or_owner",
        check_str=("rule:context_is_admin or rule:owner"),
        description="Rule for admin or owner access",
    ),
)

__all__ = ("list_rules",)
