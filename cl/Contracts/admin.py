from django.contrib import admin
from .models import Organization, Contract

admin.site.register(Contract)
admin.site.register(Organization)

# Register your models here.
