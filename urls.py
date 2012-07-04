from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from skarbonka.views import common
from skarbonka.views import jm
from skarbonka.views import miasto
from skarbonka.views import sklep
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^$',common.mainPage),
#	(r'^$',mainPage),
	(r'^jm/$',jm.jmPage),
	(r'^jm/add/$',jm.jmAdd),
	(r'^jm/edit/(\d)/$',jm.jmEdit),
	(r'^jm/edit/$',jm.jmEdit),
	(r'^jm/delete/(\d)/$',jm.jmDel),
	
	(r'^miasto/$',miasto.miastoPage),
	(r'^miasto/add/$',miasto.miastoAdd),
	(r'^miasto/edit/$',miasto.miastoEdit),
	(r'^miasto/edit/(\d)/$',miasto.miastoEdit),
	(r'^miasto/delete/(\d)$',miasto.miastoDel),

	(r'^sklep/$',sklep.SklepPage),
	(r'^sklep/add/$',sklep.SklepAdd),
	(r'^sklep/edit/(\d)/$',sklep.SklepEdit),
	(r'^sklep/delete/(\d)/$',sklep.SklepDel),

	(r'^admin/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'skarbonka.views.home', name='home'),
    # url(r'^skarbonka/', include('skarbonka.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
