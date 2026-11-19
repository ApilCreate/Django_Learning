from django.db import models

# Main purpose is to create tabels inside db
class Student(models.Model):
    username = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.username