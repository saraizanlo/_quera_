from django.db import models

class Question(models.Model):
    name = models.CharField(max_length = 30)
    form = models.TextField()
    answer = models.TextField()
    publish_date = models.DateField()
    level = models.CharField(max_length= 10)

    def __str__(self) -> str:  
        return self.name


class Lesson(models.Model):
    subject = models.CharField(max_length=25)
    text = models.TextField()   
    
    def __str__(self) -> str:  
        return self.subject