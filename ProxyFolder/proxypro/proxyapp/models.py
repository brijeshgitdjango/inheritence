from django.db import models

# Create your models here.
class Employee(models.Model):
	ename = models.CharField(max_length=30)
	sal = models.IntegerField()
	loc = models.CharField(max_length=20)

	def __str__(self):
		return self.ename

class EmpProxy(Employee):
	class Meta:
		proxy = True
