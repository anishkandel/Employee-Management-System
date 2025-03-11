from django.db import models

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    added_date = models.DateField(auto_now_add=True)
    added_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name  # Fix the typo: use `self.name` instead of `self.namecd`
    

from django.db import models


