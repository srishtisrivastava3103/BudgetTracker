from django.contrib import admin
from .models import User,Expense,Travel,Food,Misc,Entertainment,Bill, Post, Assets, Liability
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(User)
admin.site.register(Expense)
admin.site.register(Travel)
admin.site.register(Food)
admin.site.register(Bill)
admin.site.register(Entertainment)
admin.site.register(Misc)
admin.site.register(Post,PostAdmin)
admin.site.register(Assets)
admin.site.register(Liability)