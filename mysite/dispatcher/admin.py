from django.contrib import admin
from .models import Features, Producer, Trailer, TrailerInstance
# Register your models here.

class TrailerInstanceInline(admin.TabularInline):
    model = TrailerInstance
    readonly_fields = ('id',)
    can_delete = False
    extra = 0


class TrailerAdmin(admin.ModelAdmin):
    list_display = ("type", "features", "display_producer")

class TrailerInstanceAdmin(admin.ModelAdmin):
    list_display = ('trailer', 'status', 'dexpected_return')
    list_filter = ('status', 'dexpected_return')

    fieldsets = (
        ('General', {'fields': ('uuid', 'trailer')}),
        ('Availability', {'fields': ('status', 'dexpected_return')}),
    )

admin.site.register(Trailer, TrailerAdmin)
admin.site.register(Features)
admin.site.register(Producer)
admin.site.register(TrailerInstance)


