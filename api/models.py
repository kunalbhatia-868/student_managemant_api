from django.db import models

# Create your models here.


class Student(models.Model):

    GENDER = (
        ("f", "Female"),
        ("m", "Male"),
        ("u", "Undisclosed")
    )

    name = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER, null=True)
    percentage = models.FloatField()
    institute = models.ForeignKey(
        'Institute', on_delete=models.CASCADE, null=True, blank=True)


class Institute(models.Model):

    TYPES = (
        ("c", "college"),
        ("h", "high school")
    )

    name = models.CharField(max_length=200)
    type_of_institute = models.CharField(max_length=1, choices=TYPES)
