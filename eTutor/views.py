from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Room
from users.models import User
from django.conf import settings
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

def homepage(request):
    return render(request, "eTutor/homepage.html", {
})

def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'eTutor/messaging.html', {'rooms': rooms})

@login_required
def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'eTutor/messaging_detail.html', {'room': room})

def token(request):
    identity = request.GET.get('identity', request.user.username)
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = settings.TWILIO_ACCOUNT_SID
    api_key = settings.TWILIO_API_KEY
    api_secret = settings.TWILIO_API_SECRET
    chat_service_sid = settings.TWILIO_CHAT_SERVICE_SID

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    # Create a unique endpoint ID for the device
    endpoint = "MyDjangoChatRoom:{0}:{1}".format(identity, device_id)
    print(endpoint)

    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }

    return JsonResponse(response)