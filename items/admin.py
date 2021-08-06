# django
from django.contrib import admin

# models
from items.models import Category
from items.models import Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
        'created_at',
        'updated_at',
    )
    list_editable = (
        'name',
        'is_active',
    )
    list_filter = (
        'is_active',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'name',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at',)
