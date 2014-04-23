from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from resup import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'resup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_resumable/', include('admin_resumable.urls')),
    url(r'^upload/', views.upload, name='upload'),
)
