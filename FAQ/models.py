from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time
from utils.main import disable_for_loaddata


def gen_slug(s):
	new_slug = slugify(s, allow_unicode=True)
	return new_slug + '-' + str(int(time()))

@disable_for_loaddata
class Post(models.Model):
	title = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, blank=True, unique=True)
	body = models.TextField(blank=True, db_index=True)

	def get_absolute_url(self):
		return reverse('FAQ_detail_url', kwargs={'slug': self.slug})

	def get_update_url(self):
		return reverse('FAQ_update_url', kwargs={'slug': self.slug})

	def get_delete_url(self):
		return reverse('FAQ_delete_url', kwargs={'slug': self.slug})

	def save(self, *arg, **kwargs):
		if not self.id:
			self.slug = gen_slug(self.title)
		super().save(*arg, **kwargs)	

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['slug']
