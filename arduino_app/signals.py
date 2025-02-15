from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Only send email for new users
        send_mail(
            'Welcome to GEINOTECH!',
            f'Hello {instance.username},\n\nThank you for registering with GEINOTECH🎉🎉🎉🎉. We are excited to have you onboard!\n\nBest regards,\nGEINOTECH',
            'your-email@example.com',  # Replace with your sender email
            [instance.email],  # Must be a list
            fail_silently=False,
        )
