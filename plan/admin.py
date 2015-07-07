from django.contrib import admin

from plan.models.project import Project, ProjectAdmin
from plan.models.task import Task, TaskAdmin

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)

