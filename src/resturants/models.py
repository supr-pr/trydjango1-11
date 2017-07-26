from django.db import models
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator
# Create your models here.

class Resturant(models.Model):
	name			= models.CharField(max_length=120)
	location 		= models.CharField(max_length=120, null=True, blank=True)
	categories		= models.CharField(max_length=120, null=True, blank=True)
	timestamp		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	my_date_field 	= models.DateTimeField(auto_now=True, auto_now_add=False)
	slug 			= models.SlugField(null=True, blank=True)

	# show name of obj in admin
	def __str__ (self):
		return self.name

	@property
	def title(self):
		return self.name 

def res_pre_Save_reciever(sender, instance, *args, **kwargs):
	# print ('saving..')
	# print(instance.timestamp)
	if not instance.slug:
		# instance.name = "New_Title"
		instance.slug = unique_slug_generator(instance)


# def res_post_Save_reciever(sender, instance, *args, **kwargs):
# 	print ('saved')
# 	print(instance.timestamp)
# 	if not instance.slug:
# 		instance.slug = unique_slug_generator(instance)
# 		instance.save()

pre_save.connect(res_pre_Save_reciever, sender =Resturant)

# post_save.connect(res_post_Save_reciever, sender =Resturant)
