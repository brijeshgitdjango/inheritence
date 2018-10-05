from django.db import models

# Create your models here.
class CommonInfo(models.Model):
	name = models.CharField(max_length=30)
	loc = models.CharField(max_length=30)

	class Meta:
		abstract = True

class Student(CommonInfo):
	fee = models.IntegerField()

	def __str__(self):
		return self.name

class Employee(CommonInfo):
	sal = models.IntegerField()

	def __str__(self):
		return self.name