from django.conf.urls import patterns, url

from oedipus.views import PageView

urlpatterns = patterns('',
    url(r'^$', PageView.as_view(), name='index'),
    url(r'^(?P<page_name>.*)/$', PageView.as_view(), name='page'),
    )
