from django.contrib import admin
from django.utils.text import Truncator

from .models import Task
from account.models import CustomizeUser


admin.site.site_header = "DoDone app administration"


def display_content(self):
    return ''.join(self.content[:30])


def get_name(self):
    return f'{self.user.first_name} {self.user.last_name}'


def count_tasks(self):
    return f'{Task.objects.filter(user_id=self.id).count()}'


count_tasks.short_description = 'Number of tasks'
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


class TaskInline(admin.StackedInline):
    model = Task
    fields = ['title', 'content']


class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'work_position', 'email', count_tasks]
    search_fields = ['first_name', 'last_name']
    readonly_fields = ['first_name', 'last_name', 'work_position', 'email', count_tasks]
    exclude = ('password', 'last_login', 'is_superuser', 'username',
               'is_staff', 'is_active', 'date_joined', 'email_confirmed', 'groups', 'user_permissions')
    inlines = [TaskInline]
    empty_value_display = '-empty-'

    class Meta:
        model = CustomizeUser


admin.site.register(Task, TaskAdmin)
admin.site.register(CustomizeUser, AccountAdmin)
