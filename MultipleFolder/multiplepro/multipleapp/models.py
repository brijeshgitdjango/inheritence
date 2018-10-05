from django.db import models

# Create your models here.
class ModelFirst(models.Model):
	mf_id = models.IntegerField(primary_key=True)
	mf_name = models.CharField(max_length=30)

	def __str__(self):
		return self.mf_name

class ModelSecond(models.Model):
	ms_id = models.IntegerField(primary_key=True)
	ms_name = models.CharField(max_length=30)

	def __str__(self):
		return self.ms_name

class ModelMain(ModelFirst,ModelSecond):
	mm_name = models.CharField(max_length=30)

	def __str__(self):
		return self.mm_name