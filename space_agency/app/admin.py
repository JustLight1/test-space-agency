from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.html import format_html

from .models import SliderItem


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'display_small_image', 'display_big_image', 'id',
                    'my_order']
    search_fields = ['title']
    list_per_page = 20
    ordering = ['my_order']

    def display_small_image(self, obj):
        return format_html(
            '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
            obj.image.url
        )

    def display_big_image(self, obj):
        return format_html(
            '<img src="{}" style="max-height: 100px; max-width: 100px;" />',
            obj.big_image.url
        )

    display_big_image.short_description = 'Большое изображение'
    display_small_image.short_description = 'Маленькое изображение'
