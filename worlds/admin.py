from django.contrib import admin
from .models import World


@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    """Admin configuration for the World model."""

    list_display = (
        'title',
        'owner',
        'genre',
        'is_public',
        'created_at',
        'updated_at',
    )
    list_filter = ('genre', 'is_public', 'created_at')
    search_fields = ('title', 'summary', 'owner__username')