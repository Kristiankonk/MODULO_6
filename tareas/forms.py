from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TareaForm(forms.Form):
    titulo = forms.CharField(max_length=100, label="Título")
    descripcion = forms.CharField(
        widget=forms.Textarea,
        label="Descripción",
        required=False
    )

class RegistroForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        help_text="Obligatorio. Solo letras, números y @/./+/-/_",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email = forms.EmailField(
        label="Correo electrónico",
        help_text="Obligatorio. Debe ser un correo válido.",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        help_text="Debe contener al menos 8 caracteres.",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        strip=False,
        help_text="Ingresa nuevamente la contraseña.",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
