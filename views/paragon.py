from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms.models import model_to_dict
from skarbonka.towary.models import *
from skarbonka.forms import *
def ObliczWartosc(paragon):
	wynik=[]
	for i in range(0,len(paragon)):
		paragon[i].val=i*2
	return wynik
def ParagonPage(request):
	paragon=Paragon.objects.all()
	value=ObliczWartosc(paragon)
	return render_to_response('paragon_list.html',{'paragony':paragon,'value':value})
def ParagonAdd(request):
	x=3
