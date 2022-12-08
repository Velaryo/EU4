from django.db import models
from django.contrib.auth.models import User

class Proyecto(models.Model):
	foto = models.CharField(max_length=255)
	tiulo = models.CharField(max_length=200)
	desc = models.TextField()
	tags = models.CharField(max_length=200)
	url = models.URLField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=True)
 
	class Meta:
		db_table = "proyectos"
