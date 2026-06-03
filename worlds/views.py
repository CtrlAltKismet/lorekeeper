from django.shortcuts import render


def home(request):
    """Display the Lorekeeper homepage."""
    return render(request, 'worlds/home.html')