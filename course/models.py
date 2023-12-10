from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.ImageField()
    instructor = models.CharField(max_length=50)
    duration = models.DateTimeField(1)
    


    def __str__(self):
        return self.title
    
    
