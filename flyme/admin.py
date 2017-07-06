from django.contrib import admin
from flyme.models import Recall, Profile


# Register your models here.
@admin.register(Recall)
class RecallAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'thumb', 'full', 'updated', 'created']
    list_filter = ['updated']
    date_hierarchy = 'updated'
    search_fields = ['=title', '=desc']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'body1', 'body2', 'updated', 'created']
    list_filter = ['updated']
    date_hierarchy = 'updated'
    search_fields = ['=title']
