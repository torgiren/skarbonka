from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
#from skarbonka.towary.models import *
#from skarbonka.forms import *
#from django.forms.models import model_to_dict

def mainPage(request):
	return render_to_response('main.html',{})
