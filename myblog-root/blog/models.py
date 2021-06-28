from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=300)
	date = models.DateTimeField()
	text = models.TextField()
	image = models.ImageField(upload_to='event_images/')

	def get_summary(self):
		return self.text[:150]


	def __str__(self):
		return self.title
	
	