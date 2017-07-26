
# from django.views.generic.list import ListView
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render 
from django.shortcuts import get_object_or_404 
from .models import Resturant
from django.db.models import Q

# Create your views here.
# Function based view

def resturant_listview (request):
	template_name = 'resturants/resturants_list.html'
	queryset = Resturant.objects.all()
	context ={
		"object_list": queryset
	}
	return render(request, template_name,context)

class ResturantListView (ListView):
	template_name = 'resturants/resturants_list.html'
	
	def get_qureyset(self):
		slug= self.kwargs.get("slug")
		if slug:
			queryset = Resturant.objects.filter(
					Q(categories__iexact=slug) |
					Q(categories__icontains=slug)
				)
		else:
			queryset = Resturant.objects.all()
		return queryset

class ResturantDetailView(DetailView):
	queryset = Resturant.objects.all()

	def get_object(self, *args, **kwargs):
		rest_id = self.kwargs.get('rest_id')
		obj = get_object_or_404(Resturant, id=rest_id)
		return obj

	# def get_context_data(self, *args, **kwargs):

	# 	context = super(ResturantDetailView, self).get_context_data(*args, **kwargs)
	# 	return context
		

# class ResturantListView (ListView):
# 	queryset = Resturant.objects.all()
# 	template_name = 'resturants/resturants_list.html'


# class MexicanresturantListView (ListView):
# 	queryset = Resturant.objects.filter(categories__iexact='mexican')
# 	template_name = 'resturants/resturants_list.html'


# class AsianresturantListView (ListView):
# 	queryset = Resturant.objects.filter(categories__iexact='asian')
# 	template_name = 'resturants/resturants_list.html'



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




# class HomeView(TemplateView):
# 	template_name = 'home.html'

# class AboutView(TemplateView):
# 	template_name = 'about.html'

# class ContactView(TemplateView):
# 	template_name = 'contact.html'