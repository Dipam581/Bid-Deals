from django.core.mail import send_mail as django_send_mail
from django.conf import settings

def send_mail():
    subject = "Django mail"
    message = "Test mail"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["dipam.ghosh@keross.com"]
    django_send_mail(subject, message, from_email, recipient_list)