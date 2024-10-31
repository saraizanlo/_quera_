from django.db import models
from bank.models import Lesson ,Question

class Bootcamp(models.Model):
    name = models.CharField(max_length=25)
    start_date = models.DateField()
    duration = models.IntegerField()
    price = models.FloatField()

    def __str__(self) -> str:  
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=25)
    assingment = models.ManyToManyField(Question ,related_name="assignments", blank=True)
    lesson = models.ManyToManyField(Lesson , related_name="lessons", blank=True)

    def __str__(self) -> str:  
        return self.name


