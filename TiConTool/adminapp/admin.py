from django.contrib import admin

from employeeapp.models import Roles, TypeDocuments, Genre, Employees, EventsType, Permissions, PermissionsByRole

# Register your models here.
admin.site.register(Roles)
admin.site.register(TypeDocuments)
admin.site.register(Genre)
admin.site.register(Employees)
admin.site.register(EventsType)
admin.site.register(Permissions)
admin.site.register(PermissionsByRole)
