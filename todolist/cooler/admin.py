from django.contrib import admin
from .models import Taskers,Task
# Register your models here.
@admin.register(Taskers)
class TaskerAdmin(admin.ModelAdmin):
    list_display = ('username','email','create')
    search_fields = ('username','email')#enables search functions

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
     list_display = ('title','completed','create','tasker')
     search_fields = ['title','completed','tasker__username']
     list_filter = ('completed','tasker__username')
     autocomplete_fields = ('tasker',)#dropdown showing taskers#

