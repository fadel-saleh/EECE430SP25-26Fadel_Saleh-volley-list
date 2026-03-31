from django.shortcuts import render, redirect, get_object_or_404
from .models import player
from .forms import playerForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def player_list(request):
    players = player.objects.all()
    return render(request, 'player_list.html', {'players': players})

def add_player(request):
    if request.method == 'POST':
        form = playerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = playerForm()
    return render(request, 'add_player.html', {'form': form})

def update_player(request , pk):
    player_inst = get_object_or_404(player, pk=pk)
    if request.method == 'POST':
        form = playerForm(request.POST, instance=player_inst)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = playerForm(instance=player_inst)
    return render(request, 'update_player.html', {'form': form})

def delete_player(request , pk):
    player_inst = get_object_or_404(player, pk=pk)
    if request.method == 'POST':
        player_inst.delete()
        return redirect('player_list')
    return render(request, 'delete_player.html', {'player': player_inst})




