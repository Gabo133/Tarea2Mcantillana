from django.forms import ModelForm
from basket.models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['rut', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position']
        