from django.contrib import admin
from .models import Blogs


@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'heading', 'content', 'created_at', 'preview')
    list_filter = ('created_at',)
    search_fields = ('heading',)