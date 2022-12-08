from django import forms
from .models import Proyecto

class CreateProjForm(forms.ModelForm): #crea form a partir de un modelo
	class Meta: 
		model = Proyecto
		fields = ['foto', 'tiulo', 'desc', 'tags', 'url']
	# foto = forms.CharField(max_length=255)
	# tiulo = forms.CharField(max_length=200)
	# desc = forms.CharField(widget=forms.Textarea())
	# tags = forms.CharField(max_length=200)
	# url = forms.CharField(max_length=200)
