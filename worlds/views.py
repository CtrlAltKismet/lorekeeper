from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


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