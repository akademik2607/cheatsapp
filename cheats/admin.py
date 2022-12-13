from django.contrib import admin

from cheats.models import Category, Cheat


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)


@admin.register(Cheat)
class CheatsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_filter = ('title', 'status', 'created_at', 'updated_at')
