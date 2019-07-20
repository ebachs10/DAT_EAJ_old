from django.contrib import admin

from .models import Journal, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class JournalAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Journal, JournalAdmin)
admin.site.register(Comment)
