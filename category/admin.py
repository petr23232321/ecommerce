from django.contrib import admin
from category.models import Category

class CaregoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug')

admin.site.register(Category, CaregoryAdmin)



