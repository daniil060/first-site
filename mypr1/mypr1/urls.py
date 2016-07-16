from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	
   # url(r'^$', 'mypr1.views.home', name='home'),
    url(r'', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
