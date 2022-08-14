from django.contrib import admin

from task_application.models import Task
from .models import CustomizeUser


class TaskInline(admin.StackedInline):
    model = Task
    fields = ['title', 'content']


def count_tasks(self):
    return f'{Task.objects.filter(user_id=self.id).count()}'


count_tasks.short_description = 'Number of tasks'


class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'work_position', 'email', count_tasks]
    search_fields = ['first_name', 'last_name']
    exclude = ('password', 'last_login', 'is_superuser', 'username',
               'is_staff', 'is_active', 'date_joined', 'email_confirmed', 'groups', 'user_permissions')
    inlines = [TaskInline]
    empty_value_display = '-empty-'

    def has_add_permission(self, request):
        if not request.user.is_superuser:
            return False
        return True

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser:
            return False
        return True

    class Meta:
        model = CustomizeUser


admin.site.register(CustomizeUser, AccountAdmin)
