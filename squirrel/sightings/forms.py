from django.forms import ModelForm 
from .models import Squirrel
class SquirrelForm(ModelForm): 
    class META: 
        model = Squirrel 
        fields ='__all__'

