from django.contrib import admin
from .models import User,Expense,Travel,Food,Misc,Entertainment,Bill
# Register your models here.
admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Travel)
admin.site.register(Food)
admin.site.register(Bill)
admin.site.register(Entertainment)
admin.site.register(Misc)