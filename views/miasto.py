from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from skarbonka.towary.models import *
from skarbonka.forms import *
from django.forms.models import model_to_dict
from skarbonka.views.miasto import *
def miastoPage(request):
	miasto=Miasta.objects.all()
	return render_to_response('miasto_list.html',{'miasto':miasto})
def miastoAdd(request):
	if request.method=='POST':
		form=MiastoForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			miasto=Miasta(nazwa=cd['nazwa'])
			miasto.save()
		return HttpResponseRedirect('/miasto/')
	else:
		form=MiastoForm()
	return render_to_response('miasto_add_form.html',{'form':form,'action':'add'})
def miastoEdit(request,ID=-1):
	if request.method=='POST':
	#TODO sprawdzanie poprawnosci
		miasto=Miasta.objects.get(id=request.POST['id'])
		miasto.nazwa=request.POST['nazwa']
		miasto.save()
		return HttpResponseRedirect('/miasto/')
	else:
		miasto=Miasta.objects.get(id=ID)
		form=MiastoForm(model_to_dict(miasto))
	return render_to_response('miasto_add_form.html',{'form':form,'action':'edit','id':ID})
def miastoDel(request,ID):
	miasto=Miasta.objects.get(id=ID)
	miasto.delete()
	return HttpResponseRedirect('/miasto/')
