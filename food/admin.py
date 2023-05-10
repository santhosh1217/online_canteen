from django.contrib import admin
from .models import *


admin.site.register(Signup)
admin.site.register(Cart)

class FoodmenuAdmin(admin.ModelAdmin):
    List_display = ('name')
admin.site.register(Foodmenu, FoodmenuAdmin)

class BreakfastAdmin(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(Breakfast, BreakfastAdmin)

class LunchAdmin(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(Lunch, LunchAdmin)

class FastFoodAdmin(admin.ModelAdmin):
    list_display = ('name','price')

admin.site.register(FastFood, FastFoodAdmin)

class DailySpecialAdmin(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(DailySpecial, DailySpecialAdmin)

class ComboOfferAdmin(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(ComboOffer,ComboOfferAdmin)

class FreshJuiceAdmin(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(FreshJuice,FreshJuiceAdmin)

class ChatItemsAdmin(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(ChatItems,ChatItemsAdmin)



