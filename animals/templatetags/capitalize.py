from django import template

register = template.Library()

@register.filter(name='capitalize')
def capitalize(value):
    # Make the first half upper
    return value[:len(value)//2].upper() + value[len(value)//2:].lower()

@register.filter(name="check_for_hey")
def check_for_hey(value):
    if value.lower() in "hey" or value.upper() in "HEY":
        value = "Element removed by filter!"

    return value
@register.filter(name="insert_underscore_in_the_middle")
def insert_underscore_in_middle(value):
    return value[:len(value)//2] + "_" + value[len(value)//2:]



# When we use templatetags or filters we have to rebuild the project