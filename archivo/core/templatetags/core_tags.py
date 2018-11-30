from django import template
register = template.Library()

@register.simple_tag
def buscar_organismo(id_organismo, organismos):
    for organismo in organismos:
        if organismo[0]== id_organismo:
            return organismo[1]