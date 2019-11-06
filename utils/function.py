
from django.core.mail import send_mail

def sendMail(subject,from_email,to_email,signup_message):
    subject = subject
    from_email = from_email
    to_email = to_email
    signup_message = signup_message
    send_mail(subject=subject, from_email=from_email,recipient_list=to_email,message=signup_message, fail_silently=False)