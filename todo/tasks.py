from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings
from django.utils.html import strip_tags



@shared_task()
def send_email_todos(email_address, todos, from_email):
    """Sends an email when the user asks."""

    send_mail(
        subject="Your Todos",
        message=f"{todos}\n\n",
        from_email=f"{from_email}",
        recipient_list=[email_address],
        html_message=todos,

        fail_silently=False,
    )