from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index.as_view(), name="index"),
	path('create/', views.create_proj, name="create"),
	path('update/<pk>/', views.UpdateProj.as_view(), name="update"),
	path('delete/<pk>/', views.DeleteProj.as_view(), name="delete"),
	path('detail/<pk>/', views.DetailProj.as_view(), name="detail"),
	path('ips/', views.ListIp.as_view(), name="ip_list"),
	
]
