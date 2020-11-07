from django.contrib import admin
from mysite.models import PlayList , Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'vid', 'plist')

admin.site.register(PlayList)
admin.site.register(Video,VideoAdmin)
