from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from skarbonka.towary.models import *
from skarbonka.forms import *
from django.forms.models import model_to_dict
from skarbonka.views.sklep import *
def SklepPage(request):
	sklep=Sklep.objects.all()
	return render_to_response('sklep_list.html',{'sklepy':sklep})
def SklepAdd(request):
	if request.method=='POST':
		form=SklepForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			sklep=Sklep(**cd)
			sklep.save()
		return HttpResponseRedirect("/sklep/")
	else:
		form=SklepForm()
	return render_to_response('sklep_add_form.html',{'form':form,'action':'add'})
def SklepEdit(request,ID):
	if request.method=='POST':
		form=SklepForm(request.POST)
		if form.is_valid():
			sklep=Sklep.objects.get(id=ID)
			sklep.nazwa=request.POST['nazwa']
			sklep.adres=request.POST['adres']
			sklep.miasto=Miasta.objects.get(id=request.POST['miasto'])
			sklep.save()
		return HttpResponseRedirect('/sklep')
	else:
		sklep=Sklep.objects.get(id=ID)
		form=SklepForm(model_to_dict(sklep))
	return render_to_response('sklep_add_form.html',{'form':form,'action':'edit','id':ID})
def SklepDel(request,ID):
	sklep=Sklep.objects.get(id=ID)
	sklep.delete()
	return HttpResponseRedirect('/sklep')
