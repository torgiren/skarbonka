from django import forms
from skarbonka.towary.models import *
import datetime

class JMForm(forms.Form):
	nazwa=forms.CharField()
class MiastoForm(forms.Form):
	nazwa=forms.CharField()
class SklepForm(forms.Form):
	nazwa=forms.CharField()
	adres=forms.CharField()
	miasto=forms.ModelChoiceField(Miasta.objects)
class TowarForm(forms.Form):
	nazwa=forms.CharField()
	jm=forms.ModelChoiceField(JM.objects)
class ParagonForm(forms.Form):
	sklep=forms.ModelChoiceField(Sklep.objects)
	data=forms.DateTimeField()
