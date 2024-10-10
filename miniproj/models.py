from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=500)
    createdOn=models.DateTimeField(auto_now=True)
    owner=models.CharField(max_length=50,default="Anonymous")
    def __str__(self):
        return self.title
