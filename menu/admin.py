from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse

from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fields = ('title', 'menu', 'parent', 'get_link')
    readonly_fields = ('get_link', 'parent',)

    def get_link(self, obj):
        obj_admin_url = reverse('admin:menu_menuitem_change', args=(obj.id,))
        return mark_safe(f'<a href={obj_admin_url}> {obj.title} </a>')

    def get_queryset(self, request, *args, **kwargs):
        qs = super(MenuItemInline, self).get_queryset(request)
        return qs.order_by('parent__title')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    fields = ('name',)
    inlines = (MenuItemInline,)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'menu',)
    inlines = (MenuItemInline,)
