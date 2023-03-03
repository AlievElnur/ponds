from django.contrib import admin

from .models import *

class FishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class SculpturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class ChannelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class PlantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

class OtherAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')    

admin.site.register(Fish, FishAdmin)
admin.site.register(Sculptures, SculpturesAdmin)
admin.site.register(Channels, ChannelsAdmin)
admin.site.register(Plants, PlantsAdmin)
admin.site.register(Other, OtherAdmin)
