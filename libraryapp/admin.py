from django.contrib import admin
from libraryapp.models import Library

# Register your models here.
class LibraryAdmin(admin.ModelAdmin):
    list_display=['bid','bname','bauthor','bcost']

admin.site.register(Library,LibraryAdmin)
