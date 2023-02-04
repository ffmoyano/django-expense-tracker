from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class LabelColor(models.Model):
    background = models.CharField(max_length=6)
    foreground = models.CharField(max_length=6)


class ExpenseType(models.Model):
    type = models.CharField(max_length=50)
    color = models.ForeignKey('LabelColor', on_delete=models.SET_NULL, null=True)


class IncomeType(models.Model):
    type = models.CharField(max_length=50)
    color = models.ForeignKey('LabelColor', on_delete=models.SET_NULL, null=True)


class Movement(models.Model):
    abstract = True
    date = models.DateField(default=now)
    concept = models.CharField(max_length=400, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Expense(Movement):
    type = models.ForeignKey('ExpenseType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Expense: {self.id} ({self.date} {self.type} {self.concept})'


class Income(Movement):
    type = models.ForeignKey('IncomeType', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Income: {self.id} ({self.date} {self.type} {self.concept})'
