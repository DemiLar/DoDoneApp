from django.contrib import admin

from .models import Task


admin.site.site_header = "DoDone app administration"


def display_content(self):
    return ''.join(self.content[:30])


def get_name(self):
    return f'{self.user.first_name} {self.user.last_name}'


get_name.short_description = 'Author'
display_content.short_description = 'Content'


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', display_content, get_name]
    search_fields = ['title']
    list_filter = ['user']
    readonly_fields = ['user']
    exclude = ('created', 'due_date', 'done_date', 'priority', 'importance')
    empty_value_display = '-empty-'

    class Meta:
        model = Task


admin.site.register(Task, TaskAdmin)

