from django import forms
from django.db import models
from django.contrib.auth.models import User


class ExpenseType(models.TextChoices):
    WORK = "Trabajo",
    FOOD = "Comida",


class IncomeType(models.TextChoices):
    PAYROLL = "Nómina",


class Movement(models.Model):
    abstract = True
    date = models.DateTimeField(auto_now_add=True)
    concept = models.CharField(max_length=400, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Expense(Movement):
    type = models.CharField(choices=ExpenseType.choices,
                            max_length=50)

    def __str__(self):
        return f'Expense: {self.id} ({self.date} {self.type} {self.concept})'


class Income(Movement):
    type = models.CharField(choices=IncomeType.choices,
                            max_length=50)

    def __str__(self):
        return f'Income: {self.id} ({self.date} {self.type} {self.concept})'
