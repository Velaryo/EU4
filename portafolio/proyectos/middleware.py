from django.shortcuts import HttpResponse
from ipware import get_client_ip
from .models import Ip


class obtenerIP:
	# __init__ : constructor 
	def __init__(self, get_response):
		self.get_response = get_response

	#se ejecuta despues del init
	def __call__(self, request):
		#response = self.get_response(request)
		ip, is_routable = get_client_ip(request)
#		print("ip:", ip)
		res = Ip(ip=ip)
		res.save()
		

		response = self.get_response(request)
		
		return response 
	
