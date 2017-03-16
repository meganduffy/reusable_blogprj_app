"""
?P<id> - django will take a value you pass in the url and transfer it to a view as a variable called id
\d+ - id a digit (range 0-9), + means the digit is allowed to occur one or more times.
"""
from django.conf.urls import url
import views

urlpatterns = [
    # url(r'^blog/$', views.post_list, name='post_list'),
    # # ?P<id> - django will take a value you pass in the url and transfer it to a view as a variable called id
    # # \d+ - id a digit (range 0-9), + means the digit is allowed to occur one or more times.
    # url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    # url(r'^blog/top$', views.top_five),
    # url(r'^post/new/$', views.new_post, name='new_post'),
    # url(r'^blog/(?P<id>\d+)/edit$', views.edit_post),

    url(r'^$', views.post_list, name="post_list"),
    url(r'^/$', views.post_list, name="post_list"),
    url(r'^/stuff/$', views.post_list, name="post_list"),
    url(r'^(?P<id>\d+)/$', views.post_detail),
    url(r'^top/$', views.top_five, name="top_five"),
    url(r'^post/$', views.new_post, name="new_post"),
    url(r'^(?P<id>\d+)/edit$', views.edit_post, name="edit"),
]