from django.shortcuts import render, redirect
from .models import Post
from .utils import ObjectCreateMixin, ObjectUpdateMixin
from django.views.generic import View
from .form import HistoryForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.core.paginator import Paginator


def posts(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 1)

	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	context = {
		'posts': page,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url
	}


	return render(request, 'history/history_list.html', context=context)

def history_detail(request, slug):
	post = Post.objects.get(slug__iexact=slug)
	return render(request, 'history/history_detail.html', context={'post': post, 'admin_object': post, 'detail': True})

class HistoryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
	model_form = HistoryForm
	template = 'history/history_create.html'
	raise_exception = True

class HistoryUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
	model = Post
	model_form = HistoryForm
	template = 'history/history_update.html'
	raise_exception = True

class HistoryDelete(LoginRequiredMixin, View):
	def get(self, request, slug):
		post = Post.objects.get(slug__iexact=slug)
		return render(request, 'history/history_delete.html', context={'post': post, 'delete': True})

	def post(self, request, slug):
		post = Post.objects.get(slug__iexact=slug)
		post.delete()
		return redirect(reverse('history_list_url'))


