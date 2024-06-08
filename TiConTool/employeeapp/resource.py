from import_export import resources
from .models import TimesControlEvents

class TimesControlResource(resources.ModelResource):
    class Meta:
        model = TimesControlEvents