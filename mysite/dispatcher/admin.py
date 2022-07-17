from django.contrib import admin
from .models import Features, Producer, Trailer, TrailerInstance
# Register your models here.

admin.site.register(Trailer)
admin.site.register(Features)
admin.site.register(Producer)
admin.site.register(TrailerInstance)
