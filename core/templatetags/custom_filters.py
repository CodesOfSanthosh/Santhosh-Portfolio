from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Returns the string split by arg.
    """
    if value is None:
        return []
    return [s.strip() for s in value.split(arg) if s.strip()]
