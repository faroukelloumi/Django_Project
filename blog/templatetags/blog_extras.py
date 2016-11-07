from django import template

register = template.Library()

@register.filter('citation')
def citation(texte):
    return "<< %s >>" % texte