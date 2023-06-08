from django.contrib import admin
from LittleLemonApi.models import Cart, MenuItem, Category
# Register your models here.
admin.site.register(MenuItem)   
admin.site.register(Category)
admin.site.register(Cart)