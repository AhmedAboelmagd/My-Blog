from django.db import models
from django.utils import timezone
# Create your models here.

class Author(models.Model):
	'''
	Define the blog_author table
	'''
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	blo = models.TextField()

	def __str__(self):
			return self.name

class Category(models.Model):
		cat_name=models.CharField('Category name',max_length=50)
		cat_description=models.CharField('Category description',max_length=255)
		class meta:
			verbose_name_plural = 'categories'

		def __str__(self):
			return self.cat_name

class Tag(models.Model):
	tag_name=models.CharField(max_length=50)
	tag_description=models.CharField(max_length=255)

	def __str__(self):
			return self.tag_name


class Post(models.Model):
		author = models.ForeignKey('auth.User')
		title =  models.CharField(max_length=200)
		text =   models.TextField()
		created_date = models.DateTimeField(default=timezone.now)
		puplished_date = models.DateTimeField(null=True)
		categories = models.ManyToManyField(Category)
		tags = models.ManyToManyField(Tag)

		def publish(self):
			self.published_date=timezone.now()
			self.save()

		def __str__(self):
			return self.title