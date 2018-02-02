from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
        name_length = 128
	name = models.CharField(max_length=name_length, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = "Categories"
	
	def __str__(self):
		return self.name
		
class Page(models.Model):
        title_length = 128
        url_length = 200
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=title_length)
	url = models.URLField(max_length=url_length)
	views = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title
