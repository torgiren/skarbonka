from django import forms
from skarbonka.towary.models import *

class JMForm(forms.Form):
	nazwa=forms.CharField()
class MiastoForm(forms.Form):
	nazwa=forms.CharField()
class SklepForm(forms.Form):
	nazwa=forms.CharField()
	adres=forms.CharField()
	miasto=forms.ModelChoiceField(Miasta.objects)
	
