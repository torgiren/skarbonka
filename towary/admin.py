from django.contrib import admin
from skarbonka.towary.models import *

class NazwaAdmin(admin.ModelAdmin):
	list_display=('nazwa',)
class TowarAdmin(admin.ModelAdmin):
	list_display=('nazwa','jm',)
class SklepAdmin(admin.ModelAdmin):
	list_display=('nazwa','adres','miasto')
	search_fields=('nazwa','miasto')
	list_filter=('nazwa','miasto')
class ParagonAdmin(admin.ModelAdmin):
	list_display=('sklep','data',)
	filter_horizontal=('zakupy',)
	list_filter=('sklep','data')
	date_hierarchy = 'data'
class ZakupAdmin(admin.ModelAdmin):
	list_display=('towar','cena','ilosc')
admin.site.register(JM,NazwaAdmin)
admin.site.register(Towar,TowarAdmin)
admin.site.register(Miasta,NazwaAdmin)
admin.site.register(Zakup,ZakupAdmin)
admin.site.register(Sklep,SklepAdmin)
admin.site.register(Paragon,ParagonAdmin)
