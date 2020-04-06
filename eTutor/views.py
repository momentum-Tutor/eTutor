from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.http import HttpResponse
from .models import Room, Friendship, Notifications, LikeDislike
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
        return render(request, 'eTutor/homepage.html', {'allusers': allusers,})
    else: 
        return render(request, 'eTutor/welcome_page.html')

def logout(request):
    return render(request, 'eTutor/homepage.html')

@login_required
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
    else:
        grant = VideoGrant(room='Spanish')
        token.add_grant(grant)
    response = {
        'identity': identity,
        'token': token.to_jwt().decode('utf-8')
    }

    return JsonResponse(response)

@login_required
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
            f = Friendship.objects.get(user_one=user_one, user_two=user_two)
            if data.get('deleted') != None:
                f.delete()
                print('declined')
                if f.accepted_one == True:
                    notifications = Notifications.objects.get(user=user_two)
                    notifications.friend -= 1
                    notifications.total -= 1
                    notifications.save()
                else:
                    notifications = Notifications.objects.get(user=user_one)
                    notifications.friend -= 1
                    notifications.total -= 1
                    notifications.save()
                return JsonResponse({'friends': 'declined'})
            elif data.get('accepted_one') == "True":
                if f.accepted_one == True:
                    print('exists')
                    return JsonResponse({'friends': 'exists'})
                else:
                    accepted_one = bool(data.get('accepted_one'))
                    f.accepted_one = accepted_one
                    f.friends = True
                    f.new = True
                    f.accepted_notification = User.objects.get(username=user_two)
                    f.save()
                    sender_notif = Notifications.objects.get(user=user_two)
                    sender_notif.friend += 1
                    sender_notif.total += 1
                    sender_notif.save()
                    receiver_notif = Notifications.objects.get(user=user_one)
                    receiver_notif.friend -= 1
                    receiver_notif.total -= 1
                    receiver_notif.save()
                    print('accepted')
                    return JsonResponse({'friends': 'accepted'})
            else:
                if f.accepted_two == True:
                    print('exists')
                    return JsonResponse({'friends': 'exists'})
                else:
                    accepted_two = bool(data.get('accepted_two'))
                    f.accepted_two = accepted_two
                    f.friends = True
                    f.new = True
                    f.accepted_notification = User.objects.get(username=user_one)
                    f.save()
                    sender_notif = Notifications.objects.get(user=user_one)
                    sender_notif.friend += 1
                    sender_notif.total += 1
                    sender_notif.save()
                    receiver_notif = Notifications.objects.get(user=user_two)
                    receiver_notif.friend -= 1
                    receiver_notif.total -= 1
                    receiver_notif.save()
                    print('accepted')
                    return JsonResponse({'friends': 'accepted'})
            
        else:
            print('doesnt exist')
            if data.get('accepted_one') == None:
                accepted_two = bool(data.get('accepted_two'))
                friendship = Friendship(user_one=user_one, user_two=user_two, accepted_two=accepted_two)
                friendship.save()
                notifications = Notifications.objects.get(user=user_one)
                notifications.total += 1
                notifications.friend += 1
                notifications.save()
            else:
                accepted_one = bool(data.get('accepted_one'))
                friendship = Friendship(user_one=user_one, user_two=user_two, accepted_one=accepted_one)
                friendship.save()
                notifications = Notifications.objects.get(user=user_two)
                notifications.total += 1
                notifications.friend += 1
                notifications.save()
        return JsonResponse({'friends': 'sent'})
    
@login_required
def my_friends(request):
    friend_list_one = Friendship.objects.filter(user_one=request.user, friends=True)
    friend_list_two = Friendship.objects.filter(user_two=request.user, friends=True)
    return render(request, 'eTutor/my_friends.html', {'friend_list_one': friend_list_one, 'friend_list_two': friend_list_two})

@login_required
def friend_requests(request):
    request_list_one = Friendship.objects.filter(user_one=request.user, friends=False, accepted_one=False)
    request_list_two = Friendship.objects.filter(user_two=request.user, friends=False, accepted_two=False)
    new_list = Friendship.objects.filter(new=True, accepted_notification=request.user)
    return render(request, 'eTutor/friend_requests.html', {'request_list_one': request_list_one, 'request_list_two': request_list_two, 'new_list': new_list})

@csrf_exempt    
def mark_read(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        user_one = User.objects.get(username=data.get('user_one'))
        user_two = User.objects.get(username=data.get('user_two'))
        friendship = Friendship.objects.get(user_one=user_one, user_two=user_two)
        if friendship.new == False:
            return JsonResponse({'mark_read': 'already marked read'})
        friendship.new = False
        friendship.save()
        notifications = Notifications.objects.get(user=request.user)
        notifications.total -= 1
        notifications.friend -= 1
        notifications.save()
        return JsonResponse({'mark_read': 'did a thing'})
    
def get_notifications(request):
    n, created = Notifications.objects.get_or_create(user=request.user)
    data = {'total': n.total, 'dm': n.dm, 'friend': n.friend}
    return JsonResponse(data)

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
