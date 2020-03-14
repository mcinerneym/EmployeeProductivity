from django.db import models
import datetime

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length = 32)
    def __str__(self):
        return self.name

class Shift(models.Model):
    class Meta:
        ordering = ['-date']
    STATUS = (
        ("H", "Present"),
        ("C", "Call Off"),
        ("N", "No Call No Show"),
        ("L", "Late"),
        ("E", "Left Early"),
        ("M", "Medical"),
        ("Z", "Not Here Yet"),
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS, default="Z")
    reason = models.CharField(max_length=64, blank=True)
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    position = models.ForeignKey(Position, on_delete = models.SET_NULL, null=True)
    def __str__(self):
        return self.employee.name + " " + self.date.strftime("%b %d, %Y")
    

class Break(models.Model):
    scheduled_time = models.TimeField()
    break_time = models.TimeField(blank=True)
    is_lunch = models.BooleanField(default=False)
    on_break = models.BooleanField(default=False)
    return_time = models.TimeField(blank=True)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    def __str__(self):
        return self.shift.employee.name + " " + self.shift.date.strftime("%b %d, %Y") + " " + self.scheduled_time.strftime("%I:%M %p")

class Note(models.Model):
    title = models.CharField(max_length = 64)
    description = models.CharField(max_length = 1024)
    date = models.DateField()
    def __str__(self):
        return self.title + " " + self.date.strftime("%b %d, %Y")

