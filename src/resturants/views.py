import random
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

# Create your views here.
# Function based view



# SYNTAX: return render (request, "template", {}) #response 
	# return render (request, "home.html", {})
	# return HttpResponse(yohtml)

# def home(request):
# 	num = random.randint(0,100)
# 	context = {"html_var":"This is a Context variable",
# 				"bool_item": False ,
# 				"some_list": [num, random.randint(0,10), random.randint(10,20)],

# 		}


# 	return render(request, "home.html", context)

# #------------------------------------------------------------------------------------------------

# def about(request):
# 	context = {
# 		}
# 	return render(request, "about.html", context)
# #------------------------------------------------------------------------------------------------

# # def contact(request):
# # 	context = {
# # 		}
# # 	return render(request, "contact.html", context)
# #------------------------------------------------------------------------------------------------
# class ContactView(View):
#    def get(self, request, *args, **kwargs):
#    	context={}
#    	#    return HttpResponse('Hello, World!')
#    	return render(request, "contact.html", context)

class HomeView(TemplateView):
	template_name = 'home.html'

class AboutView(TemplateView):
	template_name = 'about.html'

class ContactView(TemplateView):
	template_name = 'contact.html'