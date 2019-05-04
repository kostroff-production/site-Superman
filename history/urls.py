from django.urls import path
from .views import *

urlpatterns = [
	path('history/', posts, name='history_list_url'),
	path('history/create/', HistoryCreate.as_view(), name='history_create_url'),
	path('history/<str:slug>/', history_detail, name='history_detail_url'),
	path('history/<str:slug>/update/', HistoryUpdate.as_view(), name='history_update_url'),
	path('history/<str:slug>/delete/', HistoryDelete.as_view(), name='history_delete_url')

]