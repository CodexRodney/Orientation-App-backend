from django.db import models

class Activity(models.Model):
    '''Model for the activities'''
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)


    def __str__(self):
        '''String representation of the model'''
        return self.title
    
    class Meta:
       '''Meta class for the model'''
       pass
