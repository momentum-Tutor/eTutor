from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import Room, Friendship, LikeDislike
from users.models import User
from django.conf import settings
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant, VideoGrant
from users.forms import CustomRegistrationForm, UpdateUserForm
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


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
def user_edit(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect('homepage')
    else:
        form = UpdateUserForm(instance=request.user)
    return render(request, 'eTutor/update.html', {'form':form})

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
    else:
        grant = VideoGrant(room='Spanish')
        token.add_grant(grant)
    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }

    return JsonResponse(response)

def video_chat(request):
    return render(request, 'eTutor/video_chat.html')

@login_required
def direct_message(request, slug):
    try:
        room = Room.objects.get(slug=slug)
        print('room retrieved')
        print(request.method)
    except Room.DoesNotExist:
        room = Room(name=slug, description=slug, slug=slug)
        room.save()
        print("room created")
    return render(request, 'eTutor/messaging_detail.html', {'room': room})

@csrf_exempt
def friend_request(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        user_one = User.objects.get(username=data.get('user_one'))
        user_two = User.objects.get(username=data.get('user_two'))
        if Friendship.objects.filter(user_one=user_one, user_two=user_two).exists():
            print('exists')
        else:
            print('doesnt exist')
            if data.get('accepted_one') == None:
                accepted_two = bool(data.get('accepted_two'))
                friendship = Friendship(user_one=user_one, user_two=user_two, accepted_two=accepted_two)
                friendship.save()
            else:
                accepted_one = bool(data.get('accepted_one'))
                friendship = Friendship(user_one=user_one, user_two=user_two, accepted_one=accepted_one)
                friendship.save()


        response = {"response": "response"}
        
        return JsonResponse(response)
    

def my_friends(request):
    friend_list_one = Friendship.objects.filter(user_one=request.user, friends=True)
    friend_list_two = Friendship.objects.filter(user_two=request.user, friends=True)
    return render(request, 'eTutor/my_friends.html', {'friend_list_one': friend_list_one, 'friend_list_two': friend_list_two})


@csrf_exempt
def like(request, pk):
    if request.method == "POST":
        user_one = request.user
        user_two = User.objects.get(pk=pk)
        LikeDislike.objects.create(user_one=user_one, user_two=user_two, like=True)

        response = {"response": "liked"}
        return JsonResponse(response)
    
@csrf_exempt
def dislike(request, pk):
    if request.method == "POST":
        user_one = request.user
        user_two = User.objects.get(pk=pk)
        LikeDislike.objects.create(user_one=user_one, user_two=user_two, like=False)

        response = {"response": "disliked"}
        return JsonResponse(response)
        
    

     