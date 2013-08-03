from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from jeapsns.views import hello,current_time,system_info,index_temp,hello_get,hello_getid,hello_post,hello_form,hello_delete,hello_edit,index_temp_file #using model file:index_temp_file
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeapsns.views.home', name='home'),
    # url(r'^jeapsns/', include('jeapsns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/(.)$',hello),
    url(r'^hello/$',hello_get),
    url(r'^helloid/$',hello_getid),
    url(r'^hellopost/$',hello_post),
    url(r'^helloform/$',hello_form),#using form
    url(r'^hellodel/$',hello_delete),
    url(r'^helloedit/$',hello_edit),
    url(r'^time/get/(.)$',current_time),
    url(r'^system/(.)$',system_info),
    url(r'^index_temp/(\w{1,9})$',index_temp),
    url(r'^index_temp_file/(\w*)$',index_temp_file),
    url(r'^accounts/register/$','jeapsns.views.register'),# add register function    
    url(r'^accounts/login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
    url(r'^accounts/logout/$','django.contrib.auth.views.logout'),
    url(r'^$',hello_form)
)


