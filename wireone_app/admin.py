from django.contrib import admin
from .models import DBP,TMF,Price, DAP
# Register your models here.

admin.site.register(DBP)
admin.site.register(TMF)
admin.site.register(Price)
admin.site.register(DAP)