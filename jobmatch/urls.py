from django.conf.urls import patterns, include, url
from django.contrib import admin

from auth import views as auth_views
from jobmatcher import views as jobmatch_views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jobmatch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login_user, name='login_user'),
    url(r'^jobmatch/new$', jobmatch_views.post_job, name='post_job'),
)
