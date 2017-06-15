from django.conf.urls import url

from .views import (
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
)

urlpatterns = [
    url(r'^create/$', post_create),
    url(r'^$', post_list),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]