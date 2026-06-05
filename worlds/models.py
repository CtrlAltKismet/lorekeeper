from django.conf import settings
from django.db import models


class World(models.Model):
    """A fictional world created and managed by a registered user."""

    GENRE_CHOICES = [
        ('fantasy', 'Fantasy'),
        ('sci_fi', 'Science Fiction'),
        ('horror', 'Horror'),
        ('modern', 'Modern'),
        ('historical', 'Historical'),
        ('supernatural', 'Supernatural'),
        ('other', 'Other'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='worlds'
    )
    title = models.CharField(max_length=100)
    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
        default='fantasy'
    )
    summary = models.TextField()
    main_conflict = models.TextField(blank=True)
    tone = models.CharField(max_length=100, blank=True)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Character(models.Model):
    """A character belonging to a fictional world."""
    
    world = models.ForeignKey(
        World,
        on_delete=models.CASCADE,
        related_name='characters'
    )
    
    name = models.CharField(max_length=100)
    
    role = models.CharField(
        max_length=100,
        blank=True
    )
    
    species = models.CharField(
        max_length=100,
        blank=True
    )
    
    personality = models.TextField(
        blank=True
    )
    
    backstory = models.TextField(
        blank=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name