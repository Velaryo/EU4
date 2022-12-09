from django import forms
from .models import Proyecto

class CreateProjForm(forms.ModelForm): #crea form a partir de un modelo
	class Meta: 
		model = Proyecto
		fields = ['foto', 'titulo', 'desc', 'tags', 'url']
		labels = {
			'foto': '',
			'titulo': '',
			'desc': '',
			'tags': '',
			'url': ''

        }
		widgets = {
			'foto': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingresar URL de la imagen'				
			}),
			'titulo': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingresar titulo'				
			}),
			'desc': forms.Textarea(attrs={
			'class': 'form-control',
			'placeholder': 'Ingresa descripción'				
			}),
			'tags': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingresar tags'				
			}),
			'url': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Ingresar URL'				
			})
			

		}
