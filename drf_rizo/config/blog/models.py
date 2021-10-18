from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os
import random

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_name = random.randint(1, 27634723542)
    name, ext = get_filename_ext(filename)
    # final_name = f"{new_name}{ext}"
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"img/{final_name}"

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=250,null=True)
	slug = models.SlugField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	image=models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.title


