from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class FishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")

class SculpturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")
    
class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")

class PlantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")

class OtherAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content') 

    def get_html_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")   

admin.site.register(Fish, FishAdmin)
admin.site.register(Sculptures, SculpturesAdmin)
admin.site.register(Channels, ChannelsAdmin)
admin.site.register(Plants, PlantsAdmin)
admin.site.register(Other, OtherAdmin)
