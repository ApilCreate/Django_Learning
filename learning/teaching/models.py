from django.db import models

class Teaching(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    shift = models.CharField(max_length=50)

    def __str__(self):
        return self.name

