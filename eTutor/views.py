from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

def homepage(request):
    return render(request, "eTutor/homepage.html", {
})

def messaging(request):
    sent_messages = request.user.message_sender.all()
    received_messages = request.user.message_recipient.all()
    return render(request, 'eTutor/messaging.html', {'sent_messages': sent_messages, 'received_messages': received_messages})