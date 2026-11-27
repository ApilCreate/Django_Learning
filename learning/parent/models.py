from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=120)
    address = models.TextField()
    student_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name