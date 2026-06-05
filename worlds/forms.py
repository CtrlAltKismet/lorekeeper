from django import forms
from .models import World, Character

class WorldForm(forms.ModelForm):
    """Form for users to create and edit fictional worlds."""
    
    class Meta:
        model = World
        fields = [
            'title',
            'genre',
            'summary',
            'main_conflict',
            'tone',
            'is_public',
        ]
        
        labels = {
            'title': 'World title',
            'genre': 'Genre',
            'summary': 'World summary',
            'main_conflict': 'Main conflict',
            'tone': 'Tone or mood',
            'is_public': 'Make this world public?',
        }
        
        help_texts = {
            'summary': 'Briefly describe the setting, them, or central idea of your world.',
            'main_conflict': 'Optional: describe the main problem, war, mystery, or tension.',
            'tone': 'Optional: for example, dark fantasy, gothic horror, romantic comedy.',
            'is_public': 'Public worlds can later appear in the public world library.',
        }
        
        widgets = {
            'summary': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe your world...'
            }),
            'main_conflict': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'What is the main conflict in this world?'
            }),
            'tone': forms.TextInput(attrs={
                'placeholder': 'e.g. Dark fantasy, gothic, comedy'
            }),
        }

class CharacterForm(forms.ModelForm):
    """Form for creating and editing characters."""
    
    class Meta:
        model = Character
        fields = [
            'name',
            'role',
            'species',
            'personality',
            'backstory',
        ]