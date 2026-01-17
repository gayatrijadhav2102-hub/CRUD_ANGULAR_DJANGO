from django.db import models


# Create your models here.
class Student(models.Model):
    CITY_CHOICES = (("P", "PUNE"), ("N", "NASHIK"))
    student_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    address = models.TextField()
    birth_date = models.DateField()
    is_active = models.BooleanField(default=True)


def __str__(self):
    return self.student_name
