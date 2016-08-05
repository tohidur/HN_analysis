from django.conf.urls import url

from .views import (
    get_articles_list,
)

urlpatterns = [
    # url(r'^create$', collection_create, name="create"),
    # url(r'^(?P<slug>[\w-]+)/add$', link_add, name='add'),
    # url(r'^(?P<slug>[\w-]+)(?:/(?P<tag>[\w-]+))?/$', collection_detail, name='detail'),
    # url(r'^(?P<slug>[\w-]+)/search$', search_link, name="search_link"),
    # url(r'^(?P<slug>[\w-]+)/edit$', collection_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete$', collection_delete, name='delete'),
    url(r'^$', get_articles_list, name='get_articles_list'),
    # url(r'^about$', about, name='about'),
    # url(r'^link/(?P<id>\d+)/delete$', link_delete, name='link_delete' ),
    # url(r'^(?P<slug>[\w-]+)/delete$', collection_delete, name='collection_delete'),
    # url(r'^link/(?P<id>\d+)/edit$', link_edit, name='link_edit' ),
]