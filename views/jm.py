from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from skarbonka.towary.models import *
from skarbonka.forms import *
from django.forms.models import model_to_dict
from skarbonka.views.jm import *
def jmPage(request):
	jm=JM.objects.all()
	return render_to_response('jm_list.html',{'jm':jm})
def jmAdd(request):
	if request.method=='POST':
		form=JMForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
#			jm=JM(nazwa=cd['nazwa'])
			jm=JM(**cd)
			jm.save()
		return HttpResponseRedirect('/jm/')
	else:
		form=JMForm()
	return render_to_response('jm_add_form.html',{'form':form,'action':'add'})
def jmEdit(request,ID=-1):
	if request.method=='POST':
	#TODO sprawdzanie poprawnosci
		jm=JM.objects.get(id=request.POST['id'])
		jm.nazwa=request.POST['nazwa']
		jm.save()
		return HttpResponseRedirect('/jm/')
	else:
		jm=JM.objects.get(id=ID)
		form=JMForm(model_to_dict(jm))
	return render_to_response('jm_add_form.html',{'form':form,'action':'edit','id':ID})
def jmDel(request,ID):
	jm=JM.objects.get(id=ID)
	jm.delete()
	return HttpResponseRedirect('/jm/')
