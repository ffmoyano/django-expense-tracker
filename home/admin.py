from django.contrib import admin

from home.models import IncomeType, ExpenseType, Income, Expense

admin.site.register(Income)
admin.site.register(Expense)