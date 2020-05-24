from django.db import models

# Create your models here.
class notes(models.Model):
    author_name = models.CharField(max_length=20)
    date_of_pub = models.DateField()
    department = models.CharField(max_length=20)
    name = models.CharField(max_length=20,default="unKnown")
    views = models.IntegerField(default=0)
    file = models.FileField(upload_to="storage/")
