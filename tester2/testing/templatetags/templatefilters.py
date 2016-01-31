from django import template
register = template.Library()


@register.filter
def get_type(value):
    print("widget {0}".format(value))
    return value.__class__.__name__