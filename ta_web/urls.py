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
        r'^document/(?P<pk>\d+)/$',
        views.document_detail,
        name='document_detail'
    ),

]
