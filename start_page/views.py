from django.shortcuts import render, redirect

def home(request):
	return render(request, 'start_page/start_page.html')

def archive(request):
	return render(request, 'start_page/archive.html')

def video(request):
	return render(request, 'start_page/video.html')
