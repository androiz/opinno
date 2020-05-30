from slugify import slugify
from django import template

register = template.Library()


@register.simple_tag()
def get_slug(text):
    return slugify(text)
