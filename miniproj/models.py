from django.db import models

# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=500)
    joinedon=models.DateTimeField(auto_now=True)
    department=models.CharField(max_length=50,default="Anonymous")
    def __str__(self):
        return self.name