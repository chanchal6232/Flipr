# main/views.py - UPDATE THIS FILE
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Client, ContactSubmission, NewsletterSubscription
from .serializers import ContactSerializer, NewsletterSerializer

class LandingPageView(TemplateView):
    template_name = 'main/landing.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get ALL projects and clients
        context['projects'] = Project.objects.all()
        context['clients'] = Client.objects.all()
        return context

class ProjectListView(ListView):
    model = Project
    template_name = 'main/projects.html'
    context_object_name = 'projects'  # This makes 'projects' available in template
    
    def get_queryset(self):
        # Return all projects
        return Project.objects.all().order_by('-created_at')

class ClientListView(ListView):
    model = Client
    template_name = 'main/clients.html'
    context_object_name = 'clients'  # This makes 'clients' available in template
    
    def get_queryset(self):
        # Return all clients
        return Client.objects.all().order_by('-created_at')

class ContactCreateView(CreateView):
    model = ContactSubmission
    template_name = 'main/contact.html'
    fields = ['full_name', 'email', 'mobile_number', 'city']
    success_url = reverse_lazy('contact_success')

class SubmitContactAPI(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Thank you! We will contact you soon."}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscribeNewsletterAPI(APIView):
    def post(self, request):
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            subscription, created = NewsletterSubscription.objects.get_or_create(
                email=email,
                defaults={'is_active': True}
            )
            if not created and not subscription.is_active:
                subscription.is_active = True
                subscription.save()
            
            return Response(
                {"message": "Successfully subscribed to our newsletter!"}, 
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)