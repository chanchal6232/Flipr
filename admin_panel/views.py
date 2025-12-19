from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from main.models import Project, Client, ContactSubmission, NewsletterSubscription

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_panel/dashboard.html'
    login_url = '/admin/login/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_projects'] = Project.objects.count()
        context['total_clients'] = Client.objects.count()
        context['total_contacts'] = ContactSubmission.objects.count()
        context['total_subscriptions'] = NewsletterSubscription.objects.count()
        context['recent_contacts'] = ContactSubmission.objects.order_by('-submitted_at')[:5]
        context['recent_projects'] = Project.objects.order_by('-created_at')[:3]
        return context

class ProjectManagementView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'admin_panel/projects.html'
    context_object_name = 'projects'
    paginate_by = 10

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'admin_panel/project_form.html'
    fields = ['name', 'description', 'image', 'location', 'category']
    success_url = reverse_lazy('admin_projects')

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'admin_panel/project_form.html'
    fields = ['name', 'description', 'image', 'location', 'category']
    success_url = reverse_lazy('admin_projects')

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'admin_panel/project_confirm_delete.html'
    success_url = reverse_lazy('admin_projects')