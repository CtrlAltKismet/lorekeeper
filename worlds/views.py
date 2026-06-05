from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render


from .forms import WorldForm, CharacterForm, LoreEntryForm
from .models import World, Character, LoreEntry


def home(request):
    """Display the Lorekeeper homepage."""
    return render(request, 'worlds/home.html')


def about(request):
    """Display information about the Lorekeeper application."""
    return render(request, 'worlds/about.html')


def register(request):
    """Register a new user account."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully, Welcome to Lorekeeper!')
            return redirect('home')
        
    else:
        form = UserCreationForm()
        
    return render(request, 'worlds/register.html', {'form': form})


def logout_view(request):
    """Log out the current user."""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def world_create(request):
    """Allow a logged-in user to create a new fictional world."""
    if request.method == 'POST':
        form = WorldForm(request.POST)
        
        if form.is_valid():
            world = form.save(commit=False)
            world.owner = request.user
            world.save()
            
            messages.success(request, 'World created successfully!')
            return redirect('dashboard')
    else:
        form = WorldForm()
        
    return render(request, 'worlds/world_form.html', {'form': form})


@login_required
def dashboard(request):
    """Display the logged-in user's dashboard with their own worlds."""
    worlds = World.objects.filter(owner=request.user)
    
    return render(request, 'worlds/dashboard.html', {'worlds': worlds})


@login_required
def world_detail(request, world_id):
    """Display the details of a world owned by the logged-in user."""
    world = get_object_or_404(World, id=world_id, owner=request.user)
    
    return render(request, 'worlds/world_detail.html', {'world': world})


@login_required
def world_update(request, world_id):
    """Allow a logged-in user to update one of their own worlds."""
    world = get_object_or_404(World, id=world_id, owner=request.user)
    
    if request.method == 'POST':
        form = WorldForm(request.POST, instance=world)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'World updated successfully!')
            return redirect('world_detail', world_id=world.id)
    else:
        form = WorldForm(instance=world)
        
    return render(
        request,
        'worlds/world_form.html',
        {
            'form': form,
            'world': world,
            'is_update': True,
        }
    )


@login_required
def world_delete(request, world_id):
    """Allow a logged-in user to delete one of their own worlds."""
    world = get_object_or_404(World, id=world_id, owner=request.user)
    
    if request.method == 'POST':
        world.delete()
        messages.success(request, 'World deleted successfully!')
        return redirect('dashboard')
    
    return render(request, 'worlds/world_confirm_delete.html', {'world': world})


@login_required
def character_create(request, world_id):
    """Allow a logged-in user to create a character for one of their worlds."""
    
    world = get_object_or_404(
        World,
        id=world_id,
        owner=request.user
    )
    
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        
        if form.is_valid():
            character = form.save(commit=False)
            character.world = world
            character.save()
            
            messages.success(
                request,
                'Character created successfully!'
            )
            
            return redirect(
                'world_detail',
                world_id=world.id
            )
    else:
        form = CharacterForm()
        
    return render(
        request,
        'worlds/character_form.html',
        {
            'form': form,
            'world': world,
        }
    )  
   
    
@login_required
def character_detail(request, world_id, character_id):
    """Display the details of a character belonging to one of the user's worlds."""
    
    world = get_object_or_404(
        World,
        id=world_id,
        owner=request.user
    )
    
    character = get_object_or_404(
        Character,
        id=character_id,
        world=world
    )
    
    return render(
        request,
        'worlds/character_detail.html',
        {
            'world': world,
            'character': character,
        }
    )
   
    
@login_required
def character_update(request, world_id, character_id):
    """Allow a logged-in user to update a character in one of their worlds."""
    
    world = get_object_or_404(
        World,
        id=world_id,
        owner=request.user
    )
    
    character = get_object_or_404(
        Character,
        id=character_id,
        world=world
    )
    
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance=character)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Character updated successfully!')
            return redirect(
                'character_detail',
                world_id=world.id,
                character_id=character.id
            )
    else:
        form = CharacterForm(instance=character)
        
    return render(
        request,
        'worlds/character_form.html',
        {
            'form': form,
            'world': world,
            'character': character,
            'is_update': True,
        }
    )


@login_required
def character_delete(request, world_id, character_id):
    """Allow a logged-in user to delete a character from one of their worlds."""
    
    world = get_object_or_404(
        World,
        id=world_id,
        owner=request.user
    )
    
    character = get_object_or_404(
        Character,
        id=character_id,
        world=world
    )
    
    if request.method == 'POST':
        character.delete()
        messages.success(request, 'Character deleted successfully!')
        return redirect('world_detail', world_id=world.id)
    
    return render(
        request,
        'worlds/character_confirm_delete.html',
        {
            'world': world,
            'character': character,
        }
    )
    
    
@login_required
def lore_entry_create(request, world_id):
    """Allow a logged-in user to create a lore entry for one of their worlds."""

    world = get_object_or_404(
        World,
        id=world_id,
        owner=request.user
    )
    
    if request.method == 'POST':
        form = LoreEntryForm(request.POST)
        
        form.fields['character'].queryset = world.characters.all()
        
        if form.is_valid():
            lore_entry = form.save(commit=False)
            lore_entry.world = world
            lore_entry.save()
            
            messages.success(
                request,
                'Lore entry created successfully!'
            )
            
            return redirect(
                'world_detail',
                world_id=world.id
            )
    else:
        form = LoreEntryForm()
        form.fields['character'].queryset = world.characters.all()
        
    return render(
        request,
        'worlds/lore_entry_form.html',
        {
            'form': form,
            'world': world,
        }
    )
    
    
@login_required
def lore_entry_detail(request, world_id, lore_entry_id):
    """Display the details of a lore entry belonging to one of the user's worlds."""
    
    world = get_object_or_404(
        World,
        id=world_id,
        owner=request.user
    )
    
    lore_entry = get_object_or_404(
        LoreEntry,
        id=lore_entry_id,
        world=world
    )
    
    return render(
        request,
        'worlds/lore_entry_detail.html',
        {
            'world': world,
            'lore_entry': lore_entry,
        }
    )


@login_required
def lore_entry_update(request, world_id, lore_entry_id):
    """Allow a logged-in user to update a lore entry in one of their worlds."""
    
    world = get_object_or_404(
        World,
        id=world_id,
        owner=request.user
    )
    
    lore_entry = get_object_or_404(
        LoreEntry,
        id=lore_entry_id,
        world=world
    )
    
    if request.method == 'POST':
        form = LoreEntryForm(request.POST, instance=lore_entry)
        form.fields['character'].queryset = world.characters.all()
        
        if form.is_valid():
            form.save()
            
            messages.success(
                request,
                'Lore entry updated successfully!'
            )
            
            return redirect(
                'lore_entry_detail',
                world_id=world.id,
                lore_entry_id=lore_entry.id
            )
    else:
        form = LoreEntryForm(instance=lore_entry)
        form.fields['character'].queryset = world.characters.all()
        
    return render(
        request,
        'worlds/lore_entry_form.html',
        {
            'form': form,
            'world': world,
            'lore_entry': lore_entry,
            'is_update': True,
        }
    )