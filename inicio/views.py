from django.shortcuts import render, redirect, get_object_or_404
from .forms import PokemonForm
from .models import Pokemon

def inicio(request):
    return render(request, 'index.html')

def crear_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pokemon')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_create.html', {'form': form})

def listar_pokemon(request):
    pokemones = Pokemon.objects.all()
    return render(request, 'pokemon_list.html', {'pokemones': pokemones})

def eliminar_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    if request.method == 'POST':
        pokemon.delete()
        return redirect('lista_pokemon')
    return render(request, 'eliminar_pokemon.html', {'pokemon': pokemon})
