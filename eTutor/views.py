from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Room
from users.models import User
from django.conf import settings
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

def homePage(request):
    allusers = User.objects.all()
    if request.user.is_authenticated:
        return render(request, 'eTutor/homepage.html', {'allusers': allusers})
    else: 
        return render(request, 'eTutor/welcome_page.html')

def logout(request):
    return render(request, 'eTutor/homepage.html')

def usersPage(request):
    allusers = User.objects.all()
    return render(request, 'eTutor/all_users.html', {'allusers': allusers})

@login_required
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

def direct_message(request, slug):
    return render(request, 'eTutor/direct_message.html')