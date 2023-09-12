from django.contrib import admin
from .models import Blog, Comment, Tag, Category


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status', 'featured')
    list_filter = ('status', 'featured')
    search_fields = ('title', 'author__username')

admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
