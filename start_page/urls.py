from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name = 'home_url'),
	path('archive/', archive, name='archive_url'),
	path('video/', video, name='video_url')
]