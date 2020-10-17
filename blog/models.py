from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    body = RichTextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def summary(self):
        return (self.body[:200]+'...')
    
    def prettydate(self):
        return self.pub_date.strftime('%b %e %Y')