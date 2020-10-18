from django.contrib import admin
from gallery.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = ('views',)


admin.site.register(Gallery, GalleryAdmin)
