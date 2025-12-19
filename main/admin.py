from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, Client, ContactSubmission, NewsletterSubscription

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'category', 'created_at']
    list_filter = ['category', 'created_at']
    search_fields = ['name', 'description']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'company', 'created_at']
    search_fields = ['name', 'designation', 'company']

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'city', 'submitted_at']
    list_filter = ['city', 'submitted_at']
    search_fields = ['full_name', 'email', 'city']
    readonly_fields = ['submitted_at']

@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at', 'is_active']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']