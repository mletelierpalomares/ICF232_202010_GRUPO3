from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistroUser(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'email',
            'password1',
            'password2'
        ]
        labels = [
            'Nombre de Usuario',
            'Nombre',
            'Correo',
            'Password',
            'ConfirmaPassword'
        ]
