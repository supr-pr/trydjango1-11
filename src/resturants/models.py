from django.db import models

# Create your models here.

class Resturant(models.Model):
	name			= models.CharField(max_length=120)
	location 		= models.CharField(max_length=120, null=True, blank=True)
	categories		= models.CharField(max_length=120, null=True, blank=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	my_date_field 	= models.DateTimeField(auto_now=True, auto_now_add=False)	
	# show name of obj in admin
	def __str__ (self):
		return self.name