from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView, DetailView
from .models import Proyecto
from .forms import CreateProjForm


class Index(ListView):

	model = Proyecto

	paginate_by= 10
	template_name = 'index.html'

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
			proj.users_id = request.user
			proj.save()
			return redirect('index')
	else:
		form = CreateProjForm()
	return render(request, 'create.html', {'form': form})


class UpdateProj(LoginRequiredMixin,UpdateView):
	model = Proyecto
	fields = ['foto', 'tiulo', 'desc', 'tags', 'url']
	template_name= 'update.html'
	success_url = '/' #ruta literal, no path

class DeleteProj(LoginRequiredMixin,DeleteView):
	model = Proyecto
	template_name = 'delete.html'
	success_url = '/'

class DetailProj(DetailView):
	model = Proyecto
	template_name = 'detail.html'
