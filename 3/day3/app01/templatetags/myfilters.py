from django import template

register = template.Library()

@register.filter
def filter1(value):
    return value.replace(' ','')