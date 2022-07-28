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
    list_editable = ('dexpected_return', 'status')
    list_filter = ('status', 'dexpected_return')
    search_fields = ('id', 'trailer__type')

    fieldsets = (
        (None, {
            'fields': ('trailer', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'dexpected_return', 'company')
        }),
    )


class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('axles', 'volume', 'display_trailers')

admin.site.register(Trailer, TrailerAdmin)
admin.site.register(Features, FeaturesAdmin)
admin.site.register(Producer)
admin.site.register(TrailerInstance)


