from django.urls import path
from django.views.generic import TemplateView  # ⭐ ADD THIS IMPORT
from .views import (
    LandingPageView, ProjectListView, ClientListView,
    ContactCreateView, SubmitContactAPI, SubscribeNewsletterAPI
)

urlpatterns = [
    path('', LandingPageView.as_view(), name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('contact/success/', TemplateView.as_view(template_name='main/contact_success.html'), name='contact_success'),
    path('api/contact/', SubmitContactAPI.as_view(), name='api_contact'),
    path('api/subscribe/', SubscribeNewsletterAPI.as_view(), name='api_subscribe'),
]