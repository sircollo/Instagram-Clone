from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
  subject = 'Welcome to Insta-Kram, Share, Like, Comment, Enjoy'
  sender = 'collotests@gmail.com'
  
  text_context = render_to_string('email/insta.txt',{'name':name})
  html_content = render_to_string('email/insta.html',{'name':name})
  
  msg = EmailMultiAlternatives(subject, text_context,sender,[receiver])
  msg.attach_alternative(html_content,'text/html')
  msg.send()