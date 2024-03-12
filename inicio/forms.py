from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    TIPOS_CHOICES = [
        ('...', '...'),
        ('Tipo acero', 'Tipo acero'),
        ('Tipo agua', 'Tipo agua'),
        ('Tipo bicho', 'Tipo bicho'),
        ('Tipo dragón', 'Tipo dragón'),
        ('Tipo eléctrico', 'Tipo eléctrico'),
        ('Tipo fantasma', 'Tipo fantasma'),
        ('Tipo fuego', 'Tipo fuego'),
        ('Tipo hada', 'Tipo hada'),
        ('Tipo hielo', 'Tipo hielo'),
        ('Tipo lucha', 'Tipo lucha'),
        ('Tipo normal', 'Tipo normal'),
        ('Tipo planta', 'Tipo planta'),
        ('Tipo psíquico', 'Tipo psíquico'),
        ('Tipo roca', 'Tipo roca'),
        ('Tipo siniestro', 'Tipo siniestro'),
        ('Tipo tierra', 'Tipo tierra'),
        ('Tipo veneno', 'Tipo veneno'),
        ('Tipo volador', 'Tipo volador'),
    ]
    REGIONES_CHOICES = [
        ('Kanto', 'Kanto'),
        ('Johto', 'Johto'),
        ('Hoenn', 'Hoenn'),
        ('Sinnoh', 'Sinnoh'),
        ('Teselia/Unova', 'Teselia/Unova'),
        ('Kalos', 'Kalos'),
        ('Alola', 'Alola'),
        ('Galar', 'Galar'),
        ('Paldea', 'Paldea'),
    ]
    nombre = forms.CharField(max_length=100)
    tipo = forms.ChoiceField(choices=TIPOS_CHOICES)
    region = forms.ChoiceField(choices=REGIONES_CHOICES)

    class Meta:
        model = Pokemon
        fields = ['nombre', 'tipo', 'region']