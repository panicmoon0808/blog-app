from django.db import models

# Create your models here.
class Comment(models.Model):
	author = models.CharField(max_length=100, default="User")
	content = models.TextField(default="Good!")

	def __str__(self):
		return "%s" % self.author

class Article(models.Model):
	title= models.CharField(max_length=100)
	slug= models.SlugField()
	ingredients = models.TextField()
	body= models.TextField()
	instructions = models.TextField()
	date= models.DateTimeField(auto_now_add=True)
	comments = models.ManyToManyField(Comment, verbose_name="Comment", blank=True, null=True)

	def __str__(self):
		return "%s" % self.title


	def snippet(self):
		return self.body

