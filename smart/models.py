from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class posts(models.Model):
	name=models.ForeignKey(User)
	availability=models.CharField(max_length=3)
	location=models.CharField(max_length=200)
	time=models.CharField(max_length=12)
	reason=models.CharField(max_length=200)
	
class absent(models.Model):
	name=models.ForeignKey(User)
	absent=models.BooleanField(default=True)
	time_start=models.DateField()
	time_end=models.DateField()
	
class member(models.Model):
	name=models.ForeignKey(User)
	absent=models.ForeignKey(absent)
