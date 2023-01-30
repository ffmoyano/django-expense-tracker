from django.forms import models


class Expense(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    concept = models.CharField(max_length=400, default='')