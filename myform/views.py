from django.shortcuts import render
from rest_framework import generics 
from .models import MyForm, UserSchema
from .serializers import MyFormSerializer, UserSchemaSerializer
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        message = request.POST['message']
        sender_email = request.POST['sender_email']
        receiver_email = request.POST['receiver_email']
        name = request.POST['name']
        
        # Send email using Django's send_mail function
        send_mail(
            'Contact Form',  # Subject
            message,  # Message
            sender_email,  # Sender
            [receiver_email],  # Recipient(s)
            fail_silently=False,  # Raise an exception if sending fails
        )
    return render(request, 'index.html')



class MyFormListCreate(generics.ListCreateAPIView):
    queryset = MyForm.objects.all()
    serializer_class = MyFormSerializer

class UserSchemaListCreate(generics.ListCreateAPIView):
    queryset = UserSchema.objects.all()
    serializer_class=UserSchemaSerializer