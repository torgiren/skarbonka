from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from skarbonka.towary.models import *
from skarbonka.forms import *
from django.forms.models import model_to_dict
from skarbonka.views.towar import *
def TowarPage(request):
	towar=Towar.objects.all()
	return render_to_response('towar_list.html',{'towary':towar})
def TowarAdd(request):
	if request.method=='POST':
		form=TowarForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			towar=Towar(**cd)
			towar.save()
		return HttpResponseRedirect("/towar/")
	else:
		form=TowarForm()
	return render_to_response('towar_add_form.html',{'form':form,'action':'add'})
def TowarEdit(request,ID):
	if request.method=='POST':
		form=TowarForm(request.POST)
		if form.is_valid():
			towar=Towar.objects.get(id=ID)
			towar.nazwa=request.POST['nazwa']
			towar.jm=JM.objects.get(id=request.POST['jm'])
			towar.save()
		return HttpResponseRedirect('/towar')
	else:
		towar=Towar.objects.get(id=ID)
		form=TowarForm(model_to_dict(towar))
	return render_to_response('towar_add_form.html',{'form':form,'action':'edit','id':ID})
def TowarDel(request,ID):
	towar=Towar.objects.get(id=ID)
	towar.delete()
	return HttpResponseRedirect('/towar')
