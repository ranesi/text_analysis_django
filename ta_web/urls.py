from django.conf.urls import url
from . import views

urlpatterns = [

    url(
        r'',
        views.homepage,
        name='homepage'
    ),

    # Document URLs

    url(
        r'^document/all$',
        views.show_entries,
        name='show_entries'
    ),

    url(
        r'^document/(?P<pk>\d+)/$',
        views.entry_detail,
        name='entry_detail'
    ),

    url(
        r'^document/add$',
        views.add_document,
        name='add_document'
    ),

]
