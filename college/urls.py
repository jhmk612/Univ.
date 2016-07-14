
from django.conf.urls import url, include
from django.contrib import admin
from cafe import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^post/$', views.post, name='post'),
    url(r'^post/(?P<pk>\d+)/$', views.view_post, name='view_post')
]
