from django.conf.urls import url
from .views import index,about,article_list,article_details,article_update,article_add,article_delete,comment_add
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^$',article_list, name='article-list'),
    url(r'^about$', about, name='about'),
    url(r'^(?P<slug>[\w-]+)/$', article_details, name='article-details'),
    url(r'^update/(?P<slug>[\w-]+)/$', article_update, name='article-update'),
    url(r'^add_recipe$', article_add, name='article-add'),
    url(r'^delete/(?P<slug>[\w-]+)/$', article_delete, name='article-delete'),
 	url(r'^add_comment/(?P<slug>[\w-]+)/$', comment_add, name='article-comment-add'),
]

urlpatterns += staticfiles_urlpatterns()