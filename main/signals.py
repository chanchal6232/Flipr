from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import ContactSubmission, NewsletterSubscription

@receiver(post_save, sender=ContactSubmission)
def send_contact_notification(sender, instance, created, **kwargs):
    if created:
        # In production, use Celery for async email sending
        send_mail(
            subject='New Contact Form Submission',
            message=f'New contact from {instance.full_name} ({instance.email}) from {instance.city}',
            from_email='noreply@flipr.com',
            recipient_list=['admin@flipr.com'],
            fail_silently=True,
        )

@receiver(post_save, sender=NewsletterSubscription)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Welcome to Our Newsletter!',
            message='Thank you for subscribing to our newsletter.',
            from_email='noreply@flipr.com',
            recipient_list=[instance.email],
            fail_silently=True,
        )