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
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
