from django.shortcuts import render, redirect
from django.views.generic import View
from .form import FAQForm
from .models import Post
from django.urls import reverse

def FAQ(request):
	posts = Post.objects.all()
	return render(request, 'FAQ/FAQ_list.html', context={'posts': posts})

def FAQ_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'FAQ/FAQ_detail.html', context={'post': post, 'admin_object': post, 'detail': True})

class FAQ_create(View):
	def get(self, request):
		form = FAQForm()
		return render(request, 'FAQ/create.html', context={'form': form, 'create': True})

	def post(self, request):
		bound_form = FAQForm(request.POST)

		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(new_obj)
		return render(request, 'FAQ/create.html', context={'form': bound_form})

class FAQ_update(View):
	def get(self, request, slug):
		post = Post.objects.get(slug__iexact=slug)
		bound_form = FAQForm(instance=post)
		return render (request, 'FAQ/update.html', context={'form': bound_form, 'posts': post, 'update': True})

	def post(self, request, slug):
		post = Post.objects.get(slug__iexact=slug)
		bound_form = FAQForm(request.POST, instance=post)

		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(new_obj)
		return render (request, 'FAQ/update.html', context={'form': bound_form, 'posts': post})

class FAQ_Delete(View):
	def get(self, request, slug):
		post = Post.objects.get(slug__iexact=slug)
		return render(request, 'FAQ/delete.html', context={'post': post, 'delete': True})

	def post(self, request, slug):
		post = Post.objects.get(slug__iexact=slug)
		post.delete()
		return redirect(reverse('FAQ_url'))

