from django import forms  
from CricketLiveScores.models import Player
from django.forms import fields

class PlayerForm(forms.ModelForm):  
    class Meta:  
        model = Player  
        fields = "__all__" 