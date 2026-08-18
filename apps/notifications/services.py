from django.core.mail import send_mail


def send_email(subject, body, sender, recipients):
    return send_mail(subject, body, sender, recipients)
