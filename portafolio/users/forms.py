from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):

	class Meta:
		#indicar q el formulario pertenece a un modelo
		model = User
		#podemos definir q campos seran los q mostraremos usando el
		#atributo fields
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
