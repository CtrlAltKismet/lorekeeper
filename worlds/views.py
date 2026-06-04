from django.shortcuts import render


def home(request):
    """Display the Lorekeeper homepage."""
    return render(request, 'worlds/home.html')

def about(request):
    """Display information about the Lorekeeper application."""
    return render(request, 'worlds/about.html')