from django.db import models

class JM(models.Model):
	nazwa=models.CharField(max_length=5)
	def __unicode__(self):
		return self.nazwa
class Towar(models.Model):
	nazwa=models.CharField(max_length=50)
	jm=models.ForeignKey(JM)
	def __unicode__(self):
		return self.nazwa

class Miasta(models.Model):
	nazwa=models.CharField(max_length=50)
	def __unicode__(self):
		return self.nazwa

class Zakup(models.Model):
	towar=models.ForeignKey(Towar)
	cena=models.DecimalField(max_digits=10,decimal_places=2)
	ilosc=models.DecimalField(max_digits=10,decimal_places=2)
	def __unicode__(self):
		return "%s, %s, %s"%(self.towar,self.cena,self.ilosc)

class Sklep(models.Model):
	nazwa=models.CharField(max_length=50)
	adres=models.CharField(max_length=50)
	miasto=models.ForeignKey(Miasta)
	def __unicode__(self):
		return u"%s %s"%(self.nazwa,self.miasto)

class Paragon(models.Model):
	sklep=models.ForeignKey(Sklep)
	zakupy=models.ManyToManyField(Zakup)
	data=models.DateTimeField()
	def __unicode__(self):
		return u"%s %s"%(self.sklep,self.data)
	


# Create your models here.
