from django import template

register = template.Library()

from animals.models import Animal


@register.inclusion_tag("animals/count_mammals.html")
def count_mammals():
    mammals = 0

    for a in Animal.objects.all():
        if a.is_mammal:
            mammals += 1

    context = {"mammals": mammals}


    return context
