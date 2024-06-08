from django.db import models

# Create your models here.
class Roles(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        verbose_name=("Creation date"), auto_now_add=True, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name=("Updated date"), auto_now_add=True, null=True
    )

    def __str__(self):
        return f'Rol ID: {self.id} - {self.name}'


class TypeDocuments(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        verbose_name=("Creation_date"), auto_now_add=True, null=True
    )

    updated_at = models.DateTimeField(
        verbose_name=("Updated_date"), auto_now_add=True, null=True
    )

    def __str__(self):
        return f'Tipo Documento ID: {self.id} - {self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        verbose_name=("Creation_date"), auto_now_add=True, null=True
    )

    updated_at = models.DateTimeField(
        verbose_name=("Updated_date"), auto_now_add=True, null=True
    )

    def __str__(self):
        return f'Genero ID: {self.id} - {self.name}'



class Employees(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    #Se crea foranea del tipo de genero
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    #Se crea foranea del tipo de documento que tendra
    type_document = models.ForeignKey(TypeDocuments, on_delete=models.SET_NULL, null=True)

    identifier = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    # Se crea foranea del rol que tendra
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(
        verbose_name=("Creation date"), auto_now_add=True, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name=("Updated date"), auto_now_add=True, null=True
    )

    def __str__(self):
        return f'Empleado ID: {self.id} - {self.name} {self.last_name}, email: {self.email}'



class EventsType(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        verbose_name=("Creation date"), auto_now_add=True, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name=("Updated date"), auto_now_add=True, null=True
    )

    def __str__(self):
        return f'Evento ID: {self.id} - {self.name}'


class TimesControl(models.Model):
    start_date = models.TimeField(
        null=True
    )
    end_date = models.TimeField(
        null=True
    )

    created_at = models.DateTimeField(
        verbose_name=("Creation date"), auto_now_add=True, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name=("Updated date"), auto_now_add=True, null=True
    )



class TimesControlEvents(models.Model):
    user = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True)
    time_control = models.ForeignKey(TimesControl, on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey(EventsType, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(
        verbose_name=("Creation date"), auto_now_add=True, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name=("Updated date"), auto_now_add=True, null=True
    )



class Schedules(models.Model):
    day = models.CharField(max_length=255)
    timeStart = models.TimeField(auto_now=False, auto_now_add=False)
    timeEnd = models.TimeField(auto_now=False, auto_now_add=False)

    created_at = models.DateTimeField(
        verbose_name=("Creation date"), auto_now_add=True, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name=("Updated date"), auto_now_add=True, null=True
    )

    def __str__(self):
        return f'Horarios ID: {self.id}'



class Permissions(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        verbose_name=("Creation date"), auto_now_add=True, null=True
    )
    updated_at = models.DateTimeField(
        verbose_name=("Updated date"), auto_now_add=True, null=True
    )

    def __str__(self):
        return f'Permiso ID: {self.id} - {self.name}'


class PermissionsByRole(models.Model):
    role = models.ForeignKey(Roles, on_delete=models.SET_NULL, null=True)
    permissions = models.ForeignKey(Permissions, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Permiso Por Rol ID: {self.id} - {self.role} con permiso {self.permissions}'