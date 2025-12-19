# admin_panel/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('projects/', views.ProjectManagementView.as_view(), name='admin_projects'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='admin_project_create'),
    path('projects/<int:pk>/edit/', views.ProjectUpdateView.as_view(), name='admin_project_edit'),
    path('projects/<int:pk>/delete/', views.ProjectDeleteView.as_view(), name='admin_project_delete'),
]