from django import template


register = template.Library()

@register.filter()
def check_for_g(value):
    if "g" in value:
        value = value.upper()

    return  value