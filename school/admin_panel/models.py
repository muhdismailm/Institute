from django.db import models

from django.db import models


class School(models.Model):
    name = models.CharField(max_length=150)
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class AcademicYear(models.Model):
    year_name = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.year_name


class Classroom(models.Model):
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=10)
    academic_year = models.ForeignKey(
        AcademicYear,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.class_name} - {self.section}"


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    classrooms = models.ManyToManyField(Classroom)

    def __str__(self):
        return self.subject_name