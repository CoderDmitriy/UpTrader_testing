from django import template

from ..models import Menu


register = template.Library()


@register.inclusion_tag('menu/tags/menu.html')
def draw_menu(menu_name):
    items = Menu.objects.get(name=menu_name).children.filter(parent=None)
    return {'items': items}
