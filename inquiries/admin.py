from django.contrib import admin

# Register your models here.
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'responded', 'created_at')
    list_filter = ('responded', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
