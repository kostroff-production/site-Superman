from django.urls import path
from .views import *

urlpatterns = [
	path('FAQ/', FAQ, name='FAQ_url'),
	path('FAQ/create/', FAQ_create.as_view(), name='FAQ_create_url'),
	path('FAQ/<str:slug>/', FAQ_detail, name='FAQ_detail_url'),
	path('FAQ/<str:slug>/update/', FAQ_update.as_view(), name='FAQ_update_url'),
	path('FAQ/<str:slug>/delete/', FAQ_Delete.as_view(), name='FAQ_delete_url')

]