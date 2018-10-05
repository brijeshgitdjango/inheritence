1.Abstract model is a model which contains a coomon fields of other models.

2.Django will not create a database table for abstract model because this abstract 
  model has fields of other models.

3.Django will map the common fields to their respective models at runtime.
  