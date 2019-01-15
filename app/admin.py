from django.contrib import admin
from app.models import Series, Reading, Temperature, Emissivity

# Register your models here.
admin.site.register(Series)
admin.site.register(Reading)
admin.site.register(Temperature)
admin.site.register(Emissivity)
