from django.db import models

# Create your models here.
class Course(models.Model):
	cname = models.CharField(max_length=30)
	cfee = models.IntegerField()

	def __str__(self):
		return self.cname

class Student(Course):
	sname = models.CharField(max_length=30)
	sage = models.IntegerField()

	def __str__(self):
		return self.sname

class Teacher(Student):
	tname = models.CharField(max_length=30)
	temail = models.EmailField()

	def __str__(self):
		return self.tname