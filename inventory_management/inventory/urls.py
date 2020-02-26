from django.conf.urls import url
from django.urls import path

from .views  import *
from .views_auth import *

urlpatterns = [
	url(r'^$', index, name='index'),
	path('dashboard/', dashboard, name='dashboard'),
	path('add_item/', add_item, name='add_item'),
	path(r'edit_item/<int:pk>/', edit_item, name='edit_item'),
	path(r'delete_item/<int:pk>/', delete_item, name='delete_item'),
	path(r'items/', items, name='items'),
	path(r'incoming_item/', incoming_item, name='incoming_item'),
	path(r'outgoing_item/', outgoing_item, name='outgoing_item'),

	path(r'user_login/', user_login, name='user_login'),
	path(r'user_logout/', user_logout, name='user_logout'),
]
