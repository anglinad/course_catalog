from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'lectures_amount', 'start_date', 'finish_date']
    list_filter = ['start_date', 'finish_date']
    list_editable = ['lectures_amount', 'start_date', 'finish_date']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Course, CourseAdmin)
