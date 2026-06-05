from django.contrib import admin
from .models import World, Character, LoreEntry


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
    
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    """Admin configuration for the Character model."""
    
    list_display = (
        'name',
        'world',
        'role',
        'species',
        'created_at',
    )
    
    list_filter = (
        'species',
        'created_at',
    )
    
    search_fields = (
        'name',
        'role',
        'species',
        'world__title',
    )

@admin.register(LoreEntry)
class LoreEntryAdmin(admin.ModelAdmin):
    """Admin configuration for the LoreEntry model."""
    
    list_display = (
        'title',
        'world',
        'category',
        'importance',
        'created_at',
    )
    
    list_filter = (
        'category',
        'importance',
        'created_at',
    )
    
    search_fields = (
        'title',
        'summary',
        'content',
        'world__title',
    )