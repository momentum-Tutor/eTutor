from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Messaging, User

def homepage(request):
    return render(request, "eTutor/homepage.html", {
})

def messaging(request):
    sent_messages = request.user.message_sender.all()
    received_messages = request.user.message_recipient.all()
    return render(request, 'eTutor/messaging.html', {'sent_messages': sent_messages, 'received_messages': received_messages})

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        recipient = data.get('recipient')
        message = data.get('message')
        to_user = User.objects.get(username=recipient)
        print(data)
        messaging = Messaging(sender=request.user, recipient=to_user, message=message)
        messaging.save()
        return JsonResponse({'works': 'yes'})
