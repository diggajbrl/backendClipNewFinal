from django.contrib import admin
from .models import Clipath, Subscriber

@admin.register(Clipath)
class ClipathAdmin(admin.ModelAdmin):
    list_display = ('image', 'category', 'sender', 'active', 'date')
    list_filter = ('category', 'active', 'date')
    search_fields = ('sender', 'alternative')
    readonly_fields = ('date',)
    ordering = ('-date',)

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    search_fields = ('email',)
    readonly_fields = ('date',)
    ordering = ('-date',)