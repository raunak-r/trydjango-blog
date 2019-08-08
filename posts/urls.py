from django.conf.urls import url, include

from .views import (post_create,
					post_update,
					post_delete,
					post_detail,
					post_list)

urlpatterns = [
	url(r'^create/$', post_create, name="create"),
	url(r'^(?P<pid>\d+)/edit/$', post_update, name="update"),
	url(r'^(?P<pid>\d+)/delete/$', post_delete, name="delete"),

	url(r'^(?P<pid>\d+)/$', post_detail, name="detail"),
	# http://localhost:8000/posts/detail/1/
	
	url(r'^$', post_list, name="list"),
]