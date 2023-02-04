from django.contrib import admin

from home.models import IncomeType, ExpenseType, Income, Expense, LabelColor

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(IncomeType)
admin.site.register(ExpenseType)
admin.site.register(LabelColor)