from django.contrib import admin

from api.models import TaskList, Task

admin.site.register(Task)
admin.site.register(TaskList)
