from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
#	return render(request, 'home.html', {})
#
#def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']
        
        #send an email
        send_mail(
            'a new message from: '
            +message_name, # subject
            message, # message
            message_email, # from Email
            ['louis.prefontaine.dastous@gmail.com'], # To Email
        )
        return render(request, 'home.html', {'message_name':message_name})
        
        
    else:
        return render(request, 'home.html', {})
