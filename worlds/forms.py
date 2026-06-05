from django import forms
from .models import World, Character, LoreEntry

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
        
        labels = {
            'name': 'Character name',
            'role': 'Role',
            'species': 'Species',
            'personality': 'Personality',
            'backstory': 'Backstory',
        }
        
        help_texts = {
            'role': 'Optional: hero, villain, merchant, ruler, companion, etc.',
            'species': 'Optional: human, elf, dragon, robot, etc.',
            'personality': 'Optional: describe their personality.',
            'backstory': 'Optional: add history, motivations or important events.',
        }
        
        widgets = {
            'personality': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe the character personality...'
            }),
            'backstory': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Describe the character backstory...'
            }),
        }

class LoreEntryForm(forms.ModelForm):
    """Form for creating and editing lore entries."""
    
    class Meta:
        model = LoreEntry
        fields = [
            'title',
            'category',
            'summary',
            'content',
            'importance',
            'character',
        ]
        
        labels = {
            'title': 'Lore title',
            'category': 'Category',
            'summary': 'Summary',
            'content': 'Full lore entry',
            'importance': 'Importance',
            'character': 'Related character',
        }
        
        help_texts = {
            'summary': 'Optional: add a short overview of this lore entry.',
            'content': 'Add the full lore details here.',
            'character': 'Optional: link this lore entry to a character within this world.',
        }
        
        widgets = {
            'summary': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Briefly summarise this lore entry...'
            }),
            'content': forms.Textarea(attrs={
                'rows': 8,
                'placeholder': 'Write the full lore entry here...'
            }),
        }