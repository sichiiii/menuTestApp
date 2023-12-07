from django import template
from ..models import Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(title):
    parent_menu = Menu.objects.get(title=title)
    menu_items = Menu.objects.filter(parent_menu=parent_menu)
    return {'menu_items': menu_items}
