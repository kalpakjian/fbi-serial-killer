from django.contrib import admin
from .models import FBI_Agent, Serial_Killer, Capture

admin.site.register(FBI_Agent)
admin.site.register(Serial_Killer)
admin.site.register(Capture)