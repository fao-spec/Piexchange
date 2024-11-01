from django import template

register = template.Library()

@register.filter
def range_filter(value):
    """Returns a range from 0 to the specified value."""
    return range(int(value))
