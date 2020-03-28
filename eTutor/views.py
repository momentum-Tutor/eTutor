# from django.shortcuts import render, redirect
# from django.http import JsonResponse
# from django.views.decorators.http import require_GET, require_POST
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.decorators import login_required
# import json
# from users.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .models import *
# from .forms import CreateUserForm


# def welcomePage(request):
#     return render(request, "eTutor/welcome_page.html")


# def homePage(request):
# 	if request.user.is_authenticated:
# 		return render(request, "eTutor/homepage.html")
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')
			

# 		context = {'form':form}
# 		return render(request, 'eTutor/registration_page.html', context)

# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return redirect('home')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		context = {}
# 		return render(request, 'eTutor/login_page.html', context)

# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')



   
# from django.shortcuts import render
# from django.contrib.auth import login, authenticate
# from .forms import SignUpForm
# from django.shortcuts import render, redirect

# def welcomePage(request):
#     return render(request, 'homepage.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse, JsonResponse
from users.models import User

def homePage(request):
    allusers=User.objects.exclude(username=request.user)
    if request.user.is_authenticated:
        return render(request, 'eTutor/homepage.html', {'allusers': allusers})
    else: 
        return render(request, 'eTutor/welcome_page.html')


def logout(request):
    return render(request, 'eTutor/homepage.html')

# # Sign Up View
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('homepage')
#     else:
#         form = SignUpForm()
#     return render(request,'eTutor/registration_page.html', {'form': form})