from animals.models import Animal
from django import template

register = template.Library()


@register.simple_tag()
def count_animals():
    return Animal.objects.count()


@register.inclusion_tag('animals/animals_preview.html')
def animals_preview():
    context = {"total_animals": Animal.objects.count()}
    return context
