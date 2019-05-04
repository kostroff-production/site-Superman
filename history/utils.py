from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *


class ObjectUpdateMixin:
	model = None
	model_form = None
	template = None

	def get(self, request, slug):
		obj = self.model.objects.get(slug__iexact=slug)
		bound_form = self.model_form(instance=obj)
		return render (request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj, 'update': True})

	def post(self, request, slug):
		obj = self.model.objects.get(slug__iexact=slug)
		bound_form = self.model_form(request.POST, instance=obj)

		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(new_obj)
		return render (request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

class ObjectCreateMixin:
	model_form = None
	template = None

	def get(self, request):
		form = self.model_form()
		return render(request, self.template, context={'form': form, 'create': True})

	def post(self, request):
		bound_form = self.model_form(request.POST)

		if bound_form.is_valid():
			new_obj = bound_form.save()
			return redirect(new_obj)
		return render(request, self.template, context={'form': bound_form})


