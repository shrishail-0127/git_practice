from django.contrib import admin
from . models import Bus,Tyre,Engine

# Register your models here.

admin.site.register(Bus)
admin.site.register(Tyre)
admin.site.register(Engine)