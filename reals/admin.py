from django.contrib import admin
from .models import Search


# Register your models here.
@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'price', 'beds', 'bath', 'link', 'created_at')


# admin.site.register(Search, SearchAdmin)
