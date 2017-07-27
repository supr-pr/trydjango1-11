from django import forms


class ResturantCreateForm(forms.Form):
	name			= forms.CharField()
	location 		= forms.CharField(required= False)
	categories		= forms.CharField(required= False)