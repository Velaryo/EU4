from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from .models import Proyecto, Ip
from .forms import CreateProjForm


class Index(ListView):

	model = Proyecto

	paginate_by= 3
	page_name = 'listaProj_1'
	template_name = 'index2.html'

	"""comentado por las indicaciones de que
	solo un usuario publica proyectos"""
	# def get_queryset(self):      
	# 	return Proyecto.objects.filter(user=self.request.user)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

@login_required
def create_proj(request):

	if request.method == "POST":
		form = CreateProjForm(request.POST)
		if form.is_valid():
			proj = form.save(commit=False)
			proj.user = request.user
			proj.save()
			return redirect('index')
	else:
		form = CreateProjForm()
	return render(request, 'create.html', {'form': form})


class UpdateProj(LoginRequiredMixin,UpdateView):
	model = Proyecto
	form_class = CreateProjForm
	#fields = ['foto', 'titulo', 'desc', 'tags', 'url']
	template_name= 'update.html'
	success_url = '/' #ruta literal, no path

class DeleteProj(LoginRequiredMixin,DeleteView):
	model = Proyecto
	template_name = 'delete.html'
	success_url = '/'

class DetailProj(DetailView):
	model = Proyecto
	template_name = 'detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class ListIp(LoginRequiredMixin,ListView):

	model = Ip
	paginate_by= 10
	template_name = 'listaIp.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context