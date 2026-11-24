from django.db import models

class Students(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    grade = models.IntegerField()
    address = models.TextField()
    contact = models.BigIntegerField()

    def __str__(self):
        return self.first_name
    